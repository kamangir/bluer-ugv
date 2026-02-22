#!/usr/bin/env python3
from __future__ import annotations

import time
from dataclasses import dataclass

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# GPIO: software PWM (will have some jitter under load)
import RPi.GPIO as GPIO


def clamp(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else hi if x > hi else x


@dataclass
class MotorPins:
    fwd: int
    rev: int


class Arzhang4MotorDriver(Node):
    """
    Subscribes: /cmd_vel (geometry_msgs/Twist)
    Drives: 2x motors via H-bridge (two PWM pins per motor) using RPi.GPIO software PWM.
    """

    def __init__(self) -> None:
        super().__init__("arzhang4_motor_driver")

        # ---- Parameters (tune these) ----
        # NOTE: These are BCM pin numbers (GPIOxx), not board pin numbers.
        self.declare_parameter("left_fwd_pin", 19)
        self.declare_parameter("left_rev_pin", 13)
        self.declare_parameter("right_fwd_pin", 12)
        self.declare_parameter("right_rev_pin", 18)

        # RPi.GPIO software PWM is happier at lower frequencies (e.g. 100-2000 Hz).
        # Many motor drivers accept higher, but jitter/CPU load rises fast.
        self.declare_parameter("pwm_hz", 800)

        self.declare_parameter("timeout_s", 0.35)  # deadman stop

        self.left = MotorPins(
            fwd=int(self.get_parameter("left_fwd_pin").value),
            rev=int(self.get_parameter("left_rev_pin").value),
        )
        self.right = MotorPins(
            fwd=int(self.get_parameter("right_fwd_pin").value),
            rev=int(self.get_parameter("right_rev_pin").value),
        )

        self.pwm_hz = float(self.get_parameter("pwm_hz").value)
        self.timeout_s = float(self.get_parameter("timeout_s").value)

        # ---- GPIO setup ----
        # Use BCM numbering (GPIOxx) to match typical docs and your pin values above.
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        for pin in [self.left.fwd, self.left.rev, self.right.fwd, self.right.rev]:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        # Create PWM objects (duty in 0..100)
        self.left_fwd_pwm = GPIO.PWM(self.left.fwd, self.pwm_hz)
        self.left_rev_pwm = GPIO.PWM(self.left.rev, self.pwm_hz)
        self.right_fwd_pwm = GPIO.PWM(self.right.fwd, self.pwm_hz)
        self.right_rev_pwm = GPIO.PWM(self.right.rev, self.pwm_hz)

        for pwm in [
            self.left_fwd_pwm,
            self.left_rev_pwm,
            self.right_fwd_pwm,
            self.right_rev_pwm,
        ]:
            pwm.start(0.0)

        self.last_cmd_time = 0.0
        self.stop_all()

        # ---- ROS interfaces ----
        self.sub = self.create_subscription(Twist, "/cmd_vel", self.on_cmd_vel, 10)
        self.timer = self.create_timer(0.05, self.on_timer)  # 20 Hz safety check

        self.get_logger().info(
            f"Motor driver up (RPi.GPIO). BCM pins "
            f"L({self.left.fwd},{self.left.rev}) R({self.right.fwd},{self.right.rev}), "
            f"pwm_hz={self.pwm_hz}, timeout_s={self.timeout_s}"
        )

    def duty_to_percent(self, duty_0_1: float) -> float:
        duty = clamp(duty_0_1, 0.0, 1.0)
        return float(duty * 100.0)

    def apply_motor_u(self, pins: MotorPins, u: float) -> None:
        """
        u in [-1, 1]
        For H-bridge with two PWM pins:
          u>=0 => fwd PWM, rev 0
          u<0  => fwd 0, rev PWM
        """
        u = clamp(u, -1.0, 1.0)
        mag = abs(u)

        # apply min/max duty bounds (only when nonzero)
        if mag > 1e-4:
            mag = clamp(mag, 0.0, 1.0)
        else:
            mag = 0.0

        pct = self.duty_to_percent(mag)

        # Select PWM objects based on which motor
        if pins == self.left:
            fwd_pwm = self.left_fwd_pwm
            rev_pwm = self.left_rev_pwm
        else:
            fwd_pwm = self.right_fwd_pwm
            rev_pwm = self.right_rev_pwm

        if u >= 0.0:
            fwd_pwm.ChangeDutyCycle(pct)
            rev_pwm.ChangeDutyCycle(0.0)
        else:
            fwd_pwm.ChangeDutyCycle(0.0)
            rev_pwm.ChangeDutyCycle(pct)

    def stop_all(self) -> None:
        self.left_fwd_pwm.ChangeDutyCycle(0.0)
        self.left_rev_pwm.ChangeDutyCycle(0.0)
        self.right_fwd_pwm.ChangeDutyCycle(0.0)
        self.right_rev_pwm.ChangeDutyCycle(0.0)

    def on_cmd_vel(self, msg: Twist) -> None:
        self.last_cmd_time = time.time()

        v = float(msg.linear.x)
        w = float(msg.angular.z)

        # For now: assume inputs are already normalized-ish in [-1, 1]
        v_n = clamp(v, -1.0, 1.0)
        w_n = clamp(w, -1.0, 1.0)

        # differential mix
        u_l = clamp(v_n - w_n, -1.0, 1.0)
        u_r = clamp(v_n + w_n, -1.0, 1.0)

        self.apply_motor_u(self.left, u_l)
        self.apply_motor_u(self.right, u_r)

    def on_timer(self) -> None:
        if self.last_cmd_time == 0.0:
            return
        if (time.time() - self.last_cmd_time) > self.timeout_s:
            self.stop_all()

    def destroy_node(self) -> None:
        try:
            self.stop_all()
            # Stop PWM cleanly
            for pwm in [
                self.left_fwd_pwm,
                self.left_rev_pwm,
                self.right_fwd_pwm,
                self.right_rev_pwm,
            ]:
                pwm.stop()
            GPIO.cleanup()
        finally:
            super().destroy_node()


def main() -> None:
    rclpy.init()
    node = Arzhang4MotorDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()

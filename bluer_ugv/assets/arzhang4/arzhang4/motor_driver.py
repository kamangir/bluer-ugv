#!/usr/bin/env python3
from __future__ import annotations

import time
from dataclasses import dataclass

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import pigpio  # sudo apt install pigpio python3-pigpio


def clamp(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else hi if x > hi else x


@dataclass
class MotorPins:
    fwd: int
    rev: int


class Arzhang4MotorDriver(Node):
    """
    Subscribes: /cmd_vel (geometry_msgs/Twist)
    Drives: 2x motors via H-bridge (two PWM pins per motor)
    """

    def __init__(self) -> None:
        super().__init__("arzhang4_motor_driver")

        # ---- Parameters (tune these) ----
        self.declare_parameter("left_fwd_pin", 19)
        self.declare_parameter("left_rev_pin", 13)
        self.declare_parameter("right_fwd_pin", 12)
        self.declare_parameter("right_rev_pin", 18)

        self.declare_parameter("pwm_hz", 20000)  # typical for DC motor driver
        self.declare_parameter("timeout_s", 0.35)  # deadman stop

        self.left = MotorPins(
            fwd=int(self.get_parameter("left_fwd_pin").value),
            rev=int(self.get_parameter("left_rev_pin").value),
        )
        self.right = MotorPins(
            fwd=int(self.get_parameter("right_fwd_pin").value),
            rev=int(self.get_parameter("right_rev_pin").value),
        )

        self.pwm_hz = int(self.get_parameter("pwm_hz").value)
        self.timeout_s = float(self.get_parameter("timeout_s").value)

        # ---- pigpio ----
        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise RuntimeError(
                "pigpio daemon not running. Try: sudo systemctl enable --now pigpiod"
            )

        for pin in [self.left.fwd, self.left.rev, self.right.fwd, self.right.rev]:
            self.pi.set_mode(pin, pigpio.OUTPUT)
            self.pi.set_PWM_frequency(pin, self.pwm_hz)
            self.pi.set_PWM_range(pin, 255)  # 8-bit duty for simplicity

        self.last_cmd_time = 0.0
        self.stop_all()

        # ---- ROS interfaces ----
        self.sub = self.create_subscription(Twist, "/cmd_vel", self.on_cmd_vel, 10)
        self.timer = self.create_timer(0.05, self.on_timer)  # 20 Hz safety check

        self.get_logger().info(
            f"Motor driver up. pins L({self.left.fwd},{self.left.rev}) R({self.right.fwd},{self.right.rev}), "
            f"pwm_hz={self.pwm_hz}, timeout_s={self.timeout_s}"
        )

    def duty_to_u8(self, duty_0_1: float) -> int:
        duty = clamp(duty_0_1, 0.0, 1.0)
        return int(round(duty * 255))

    def apply_motor_u(self, pins: MotorPins, u: float) -> None:
        """
        u in [-1, 1]
        """
        u = clamp(u, -1.0, 1.0)
        mag = abs(u)

        duty = clamp(mag, 0.0, 1.0)
        pwm = self.duty_to_u8(duty)

        if u >= 0.0:
            self.pi.set_PWM_dutycycle(pins.fwd, pwm)
            self.pi.set_PWM_dutycycle(pins.rev, 0)
        else:
            self.pi.set_PWM_dutycycle(pins.fwd, 0)
            self.pi.set_PWM_dutycycle(pins.rev, pwm)

    def stop_all(self) -> None:
        for pin in [self.left.fwd, self.left.rev, self.right.fwd, self.right.rev]:
            self.pi.set_PWM_dutycycle(pin, 0)

    def on_cmd_vel(self, msg: Twist) -> None:
        self.last_cmd_time = time.time()

        v = float(msg.linear.x)
        w = float(msg.angular.z)

        # normalize into roughly [-1,1] commands
        v_n = clamp(v, -1.0, 1.0)
        w_n = clamp(w, -1.0, 1.0)

        # differential mix (simple + works even without real units)
        # left = v - w, right = v + w
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
            self.pi.stop()
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

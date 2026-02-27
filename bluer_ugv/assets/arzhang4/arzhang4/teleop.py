#!/usr/bin/env python3
from __future__ import annotations

import sys
import time
import select
import termios
import tty

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RawTerminal:
    """Put terminal into raw mode and restore on exit."""

    def __init__(self) -> None:
        self.fd = sys.stdin.fileno()
        self.old = termios.tcgetattr(self.fd)

    def __enter__(self) -> "RawTerminal":
        tty.setraw(self.fd)
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old)


def read_key_nonblocking(timeout_s: float = 0.0) -> str:
    """Return one char if available, else ''."""
    r, _, _ = select.select([sys.stdin], [], [], timeout_s)
    if not r:
        return ""
    ch = sys.stdin.read(1)
    return ch


class KeyboardTeleop(Node):
    def __init__(self) -> None:
        super().__init__("arzhang4_keyboard_teleop")

        # --- Params you may want to tune ---
        self.declare_parameter("topic", "/cmd_vel")
        self.declare_parameter("rate_hz", 20.0)

        # Map speed level [-5..+5] to linear.x in [-max_linear..+max_linear]
        self.declare_parameter("max_linear", 1.0)

        # Turning while pressed (via key-repeat). angular.z = +/- max_angular
        self.declare_parameter("max_angular", 1.0)

        # If we don't see another a/d within this time, stop turning.
        self.declare_parameter("turn_hold_s", 0.18)

        self.topic = str(self.get_parameter("topic").value)
        self.rate_hz = float(self.get_parameter("rate_hz").value)
        self.max_linear = float(self.get_parameter("max_linear").value)
        self.max_angular = float(self.get_parameter("max_angular").value)
        self.turn_hold_s = float(self.get_parameter("turn_hold_s").value)

        self.pub = self.create_publisher(Twist, self.topic, 10)

        # Speed “setpoint level” in [-5..+5]
        self.speed_level = 0  # int

        # Turning state (momentary)
        self.turn_dir = 0  # -1 right, +1 left
        self.last_turn_key_t = 0.0

        # Main loop timer (publishes Twist regularly)
        dt = 1.0 / max(1.0, self.rate_hz)
        self.timer = self.create_timer(dt, self.on_timer)

        self.get_logger().info(
            "Keyboard teleop up.\n"
            "  w/s: speed level +1/-1 (range -5..+5)\n"
            "  a/d: turn left/right while held (key repeat)\n"
            "  space or x: stop\n"
            "  q: quit\n"
            f"Publishing to {self.topic} @ {self.rate_hz} Hz"
        )

    def _apply_key(self, ch: str) -> None:
        now = time.time()

        if ch == "w":
            self.speed_level = min(5, self.speed_level + 1)
        elif ch == "s":
            self.speed_level = max(-5, self.speed_level - 1)
        elif ch == "a":
            self.turn_dir = +1
            self.last_turn_key_t = now
        elif ch == "d":
            self.turn_dir = -1
            self.last_turn_key_t = now
        elif ch == " " or ch == "x":
            self.speed_level = 0
            self.turn_dir = 0
            self.last_turn_key_t = 0.0
        elif ch == "q":
            raise KeyboardInterrupt

    def _publish(self) -> None:
        # Stop turning if key-repeat isn't continuing
        if self.turn_dir != 0 and self.last_turn_key_t > 0.0:
            if (time.time() - self.last_turn_key_t) > self.turn_hold_s:
                self.turn_dir = 0

        # Convert level -> linear speed
        linear = (self.speed_level / 5.0) * self.max_linear
        angular = float(self.turn_dir) * self.max_angular

        msg = Twist()
        msg.linear.x = float(linear)
        msg.angular.z = float(angular)
        self.pub.publish(msg)

    def on_timer(self) -> None:
        # Read all available keys quickly (nonblocking)
        while True:
            ch = read_key_nonblocking(timeout_s=0.0)
            if not ch:
                break
            try:
                self._apply_key(ch)
            except KeyboardInterrupt:
                raise

        self._publish()


def main() -> None:
    rclpy.init()

    node = KeyboardTeleop()

    try:
        # Must run in a real terminal (not in some IDE consoles)
        with RawTerminal():
            rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Send a final stop for safety
        try:
            stop = Twist()
            node.pub.publish(stop)
            time.sleep(0.05)
        except Exception:
            pass

        try:
            node.destroy_node()
        except Exception:
            pass

        try:
            if rclpy.ok():
                rclpy.shutdown()
        except Exception:
            pass


if __name__ == "__main__":
    main()

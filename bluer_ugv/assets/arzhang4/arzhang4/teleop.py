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


def fmt_char(ch: str) -> str:
    """Human-friendly representation of a possibly-nonprintable character."""
    if ch == "":
        return "<EMPTY>"
    o = ord(ch)
    if 32 <= o <= 126:
        return f"'{ch}' (ord={o})"
    return f"<0x{o:02x}> (ord={o})"


class Arzhang4KeyboardTeleop(Node):
    def __init__(self) -> None:
        super().__init__("arzhang4_keyboard_teleop")

        # --- Params ---
        self.declare_parameter("topic", "/cmd_vel")
        self.declare_parameter("rate_hz", 20.0)
        self.declare_parameter("max_linear", 1.0)
        self.declare_parameter("max_angular", 1.0)
        self.declare_parameter("turn_hold_s", 0.18)

        # Debug params
        self.declare_parameter("debug", True)
        self.declare_parameter("debug_heartbeat_s", 1.0)
        self.declare_parameter("debug_log_all_keys", True)  # log even w/s/a/d

        self.topic = str(self.get_parameter("topic").value)
        self.rate_hz = float(self.get_parameter("rate_hz").value)
        self.max_linear = float(self.get_parameter("max_linear").value)
        self.max_angular = float(self.get_parameter("max_angular").value)
        self.turn_hold_s = float(self.get_parameter("turn_hold_s").value)

        self.debug = bool(self.get_parameter("debug").value)
        self.debug_heartbeat_s = float(self.get_parameter("debug_heartbeat_s").value)
        self.debug_log_all_keys = bool(self.get_parameter("debug_log_all_keys").value)

        self.pub = self.create_publisher(Twist, self.topic, 10)

        # State
        self.speed_level = 0  # int in [-5..5]
        self.turn_dir = 0  # -1 right, +1 left
        self.last_turn_key_t = 0.0

        # Debug state
        self._last_heartbeat_t = 0.0
        self._last_publish_t = 0.0
        self._last_key_t = 0.0
        self._keys_seen = 0

        # Timer
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

        if self.debug:
            self.get_logger().info(
                "DEBUG ON\n"
                f"stdin.isatty()={sys.stdin.isatty()}  "
                f"fileno={sys.stdin.fileno()}  "
                f"sys.stdin={type(sys.stdin)}"
            )
            try:
                self.get_logger().info(
                    f"stdout.isatty()={sys.stdout.isatty()}  fileno={sys.stdout.fileno()}"
                )
            except Exception:
                pass

    def _dbg(self, msg: str) -> None:
        if self.debug:
            self.get_logger().info(msg)

    def _apply_key(self, ch: str) -> None:
        now = time.time()

        if ch == "w":
            self.speed_level = min(5, self.speed_level + 1)
            self._dbg(f"KEY w -> speed_level={self.speed_level}")
        elif ch == "s":
            self.speed_level = max(-5, self.speed_level - 1)
            self._dbg(f"KEY s -> speed_level={self.speed_level}")
        elif ch == "a":
            self.turn_dir = +1
            self.last_turn_key_t = now
            self._dbg("KEY a -> turn_dir=+1 (left)")
        elif ch == "d":
            self.turn_dir = -1
            self.last_turn_key_t = now
            self._dbg("KEY d -> turn_dir=-1 (right)")
        elif ch in [" ", "x"]:
            self.speed_level = 0
            self.turn_dir = 0
            self.last_turn_key_t = 0.0
            self._dbg("KEY stop -> speed_level=0, turn_dir=0")
        elif ch == "q":
            self._dbg("KEY q -> quitting")
            raise KeyboardInterrupt
        else:
            # Unknown key: log it (important!)
            self._dbg(f"KEY unknown: {fmt_char(ch)}")

    def _publish(self) -> None:
        # Stop turning if key-repeat isn't continuing
        if self.turn_dir != 0 and self.last_turn_key_t > 0.0:
            if (time.time() - self.last_turn_key_t) > self.turn_hold_s:
                self.turn_dir = 0
                self._dbg("turn hold expired -> turn_dir=0")

        linear = (self.speed_level / 5.0) * self.max_linear
        angular = float(self.turn_dir) * self.max_angular

        msg = Twist()
        msg.linear.x = float(linear)
        msg.angular.z = float(angular)
        self.pub.publish(msg)

        self._last_publish_t = time.time()

    def on_timer(self) -> None:
        now = time.time()

        # Heartbeat proves timer is firing even if keys don't show
        if self.debug and (now - self._last_heartbeat_t) >= self.debug_heartbeat_s:
            self._last_heartbeat_t = now
            self._dbg(
                f"heartbeat: keys_seen={self._keys_seen}, "
                f"speed_level={self.speed_level}, turn_dir={self.turn_dir}, "
                f"dt_since_last_key={now - self._last_key_t:.2f}s"
            )

        # Read all available keys quickly (nonblocking)
        while True:
            # We can also debug select() readiness by doing a tiny timeout
            ch = read_key_nonblocking(timeout_s=0.0)
            if not ch:
                break

            self._keys_seen += 1
            self._last_key_t = now

            # Log raw keys (even w/s/a/d) if requested
            if self.debug and self.debug_log_all_keys:
                self._dbg(f"raw read: {fmt_char(ch)}")

            self._apply_key(ch)

        self._publish()


def main() -> None:
    rclpy.init()
    node = Arzhang4KeyboardTeleop()

    try:
        # Must run in a real terminal
        with RawTerminal():
            rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # final stop
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

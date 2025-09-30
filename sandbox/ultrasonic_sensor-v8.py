# continues -v7

from RPi import GPIO
import argparse
import time

from bluer_ugv.logger import logger
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.classes import (
    ClassicalUltrasonicSensor,
)

parser = argparse.ArgumentParser(description="HC-SR04 single-sensor test")
parser.add_argument(
    "--side",
    type=str,
    choices=["left", "right"],
    required=True,
    help="Which sensor to read",
)
parser.add_argument(
    "--max_m",
    type=float,
    default=0.8,
    help="Detection threshold in meters (default: 0.8 m)",
)
args = parser.parse_args()

ultrasonic_sensor = ClassicalUltrasonicSensor(
    side=args.side,
    setmode=True,
)
if not ultrasonic_sensor.valid:
    raise RuntimeError(f"{args.side}: sensor not found.")


# Constants
C = 343.0  # speed of sound (m/s)
THRESH_S = (2 * args.max_m) / C  # round-trip time threshold
CYCLE_MIN_S = 0.060  # ≥60 ms per datasheet
TRIG_PULSE_S = 30e-6  # 30 µs trigger
WAIT_HIGH_TIMEOUT_S = 0.025  # 25 ms to see rising edge
WAIT_LOW_TIMEOUT_S = 0.040  # 40 ms max pulse width


def monotonic_s():
    return time.monotonic_ns() * 1e-9


logger.info(
    f"[{args.side}] Using TRIG=GPIO{ultrasonic_sensor.TRIG}, ECHO=GPIO{ultrasonic_sensor.ECHO}"
)
logger.info(f"Detect < {int(args.max_m*1000)} mm (pulse < {THRESH_S*1000:.2f} ms)")

try:
    while True:
        cycle_start = monotonic_s()

        # Trigger pulse
        GPIO.output(ultrasonic_sensor.TRIG, GPIO.LOW)
        time.sleep(200e-6)  # settle
        GPIO.output(ultrasonic_sensor.TRIG, GPIO.HIGH)
        time.sleep(TRIG_PULSE_S)  # 30 µs
        GPIO.output(ultrasonic_sensor.TRIG, GPIO.LOW)

        # Wait for rising edge
        t0 = monotonic_s()
        while (
            GPIO.input(ultrasonic_sensor.ECHO) == 0
            and (monotonic_s() - t0) < WAIT_HIGH_TIMEOUT_S
        ):
            pass
        if GPIO.input(ultrasonic_sensor.ECHO) == 0:
            logger.info("no object (no echo high)")
        else:
            t_rise = monotonic_s()

            # Wait for falling edge
            t_fall_deadline = t_rise + WAIT_LOW_TIMEOUT_S
            while (
                GPIO.input(ultrasonic_sensor.ECHO) == 1
                and monotonic_s() < t_fall_deadline
            ):
                pass

            if GPIO.input(ultrasonic_sensor.ECHO) == 1:
                logger.info("no object (pulse timeout)")
            else:
                t_fall = monotonic_s()
                pulse_s = t_fall - t_rise
                pulse_ms = pulse_s * 1000
                distance_m = (pulse_s * C) / 2
                distance_mm = distance_m * 1000

                echo_detected = 0 < pulse_s < THRESH_S

                logger.info(
                    "{}: {}  | pulse={:6.2f} ms | dist≈{:5.0f} mm".format(
                        args.side,
                        "echo detected" if echo_detected else "no object",
                        pulse_ms,
                        distance_mm,
                    )
                )

        # Keep cycle rate sane
        elapsed = monotonic_s() - cycle_start
        if elapsed < CYCLE_MIN_S:
            time.sleep(CYCLE_MIN_S - elapsed)

except KeyboardInterrupt:
    logger.info("^C detected.")
finally:
    GPIO.cleanup()

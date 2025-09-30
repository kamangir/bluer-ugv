# continues -v7

from RPi import GPIO
import argparse

from bluer_ugv.logger import logger
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.classes import (
    ClassicalUltrasonicSensor,
)

parser = argparse.ArgumentParser(description="HC-SR04 single-sensor test")
parser.add_argument(
    "--max_m",
    type=float,
    default=0.8,
    help="Detection threshold in meters (default: 0.8 m)",
)
args = parser.parse_args()

left_ultrasonic_sensor = ClassicalUltrasonicSensor(
    side="left",
    max_m=args.max_m,
)
if not left_ultrasonic_sensor.valid:
    raise RuntimeError(f"{args.side}: sensor not found.")

right_ultrasonic_sensor = ClassicalUltrasonicSensor(
    side="right",
    setmode=False,
    max_m=args.max_m,
)
if not right_ultrasonic_sensor.valid:
    raise RuntimeError(f"{args.side}: sensor not found.")


try:
    while True:
        success, echo_detected, pulse_ms, distance_mm = left_ultrasonic_sensor.detect()
        if not success:
            break

        success, echo_detected, pulse_ms, distance_mm = right_ultrasonic_sensor.detect()
        if not success:
            break
except KeyboardInterrupt:
    logger.info("^C detected.")
finally:
    GPIO.cleanup()

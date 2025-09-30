# continues -v7

from RPi import GPIO
import argparse

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
    max_m=args.max_m,
)
if not ultrasonic_sensor.valid:
    raise RuntimeError(f"{args.side}: sensor not found.")


try:
    while True:
        success, echo_detected, pulse_ms, distance_mm = ultrasonic_sensor.detect()
except KeyboardInterrupt:
    logger.info("^C detected.")
finally:
    GPIO.cleanup()

# continues -v7

from RPi import GPIO
import argparse

from bluer_ugv.logger import logger
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.pack import (
    UltrasonicSensorPack,
)

parser = argparse.ArgumentParser(description="HC-SR04 single-sensor test")
parser.add_argument(
    "--max_m",
    type=float,
    default=0.8,
    help="Detection threshold in meters (default: 0.8 m)",
)
args = parser.parse_args()

ultrasonic_sensor_pack = UltrasonicSensorPack(max_m=args.max_m)
if not ultrasonic_sensor_pack.valid:
    raise RuntimeError("at least one sensor not found.")


try:
    while True:
        success, detection = ultrasonic_sensor_pack.detect()
        if not success:
            break
except KeyboardInterrupt:
    logger.info("^C detected.")
finally:
    GPIO.cleanup()

# continues -v7

from typing import List
from RPi import GPIO

from bluer_ugv.logger import logger
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.pack import (
    ClassicalUltrasonicSensorPack,
    Detection,
)


def test(
    object_name: str,
    max_m: float = 0.8,
    graph: bool = True,
    log: bool = True,
) -> bool:
    ultrasonic_sensor_pack = ClassicalUltrasonicSensorPack(max_m=max_m)
    if not ultrasonic_sensor_pack.valid:
        return False

    list_of_detection: List[Detection] = []

    success = True
    try:
        while True:
            success, detection = ultrasonic_sensor_pack.detect(log=log)
            if not success:
                break

            if graph:
                list_of_detection.append(detection)
    except KeyboardInterrupt:
        logger.info("^C detected.")
    finally:
        GPIO.cleanup()

    if graph:
        ...

    return success

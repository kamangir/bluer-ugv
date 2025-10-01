from bluer_objects.env import abcli_object_name

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.pack import (
    UltrasonicSensorPack,
)
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.log import (
    UltrasonicSensorDetectionLog,
)
from bluer_ugv.logger import logger


class ClassicalUltrasonicSensor:
    def __init__(self):
        self.enabled = env.BLUER_UGV_ULTRASONIC_SENSOR_ENABLED == 1
        logger.info(
            "{}: {}".format(
                self.__class__.__name__,
                "enabled" if self.enabled else "disabled",
            )
        )

        self.pack = None

        self.log = (
            UltrasonicSensorDetectionLog()
            if env.BLUER_UGV_ULTRASONIC_SENSOR_KEEP_LOG == 1
            else None
        )

    def cleanup(self):
        if self.log is not None:
            self.log.export(object_name=abcli_object_name)

    def initialize(self) -> bool:
        if self.enabled:
            self.pack = UltrasonicSensorPack(
                setmode=False,
                max_m=env.BLUER_UGV_ULTRASONIC_SENSOR_MAX_M,
            )

        return self.pack.valid

    def update(self) -> bool:
        success, detection = self.pack.detect(log=log)
        if not success:
            return success

        if self.log is not None:
            self.log.append(detection)

        return True

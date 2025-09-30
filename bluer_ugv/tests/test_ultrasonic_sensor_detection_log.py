from bluer_objects import objects

from bluer_ugv.tests.ultrasonic_sensor_detection_log import test_object
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.log import (
    UltrasonicSensorDetectionLog,
)


def test_ultrasonic_sensor_detection_log(test_object):
    detection_log = UltrasonicSensorDetectionLog()

    object_name = objects.unique_object("test_ultrasonic_sensor_detection_log")

    assert detection_log.load(object_name=test_object)

    assert detection_log.export(object_name=object_name)

    assert detection_log.save(object_name=object_name)

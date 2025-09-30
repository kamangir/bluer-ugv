from bluer_ugv.tests.ultrasonic_sensor_detection_log import test_object
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.review import review


def test_ultrasonic_sensor_detection_log_review(test_object):
    assert review(
        object_name=test_object,
        export_gif=True,
    )

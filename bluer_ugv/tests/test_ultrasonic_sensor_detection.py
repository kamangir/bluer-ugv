from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import Detection
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.log import (
    UltrasonicSensorDetectionLog,
)


def test_ultrasonic_sensor_detection():
    detection = Detection(side="left")
    assert isinstance(detection, Detection)
    assert isinstance(detection.as_str(), str)

    detection = Detection(
        side="left",
        detection=False,
        reason="pulse timeout",
    )
    assert isinstance(detection.as_str(), str)

    detection = Detection(
        side="left",
        detection=False,
        reason="no echo high",
    )
    assert isinstance(detection.as_str(), str)

    detection = Detection(
        side="left",
        detection=True,
        echo_detected=False,
        pulse_ms=4.0,
        distance_mm=700.0,
    )
    assert isinstance(detection.as_str(), str)

    detection = Detection(
        side="left",
        detection=True,
        echo_detected=True,
        pulse_ms=4.0,
        distance_mm=700.0,
    )
    assert isinstance(detection.as_str(), str)

    as_dict = detection.as_dict()
    assert isinstance(as_dict, dict)
    for field in [
        "side",
        "detection",
        "reason",
        "echo_detected",
        "pulse_ms",
        "distance_mm",
    ]:
        assert field in as_dict

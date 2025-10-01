import numpy as np

from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import (
    Detection,
    DetectionState,
)

# test assets are separated from the tests
# to make them accessible externally.


def ultrasonic_sensor_detection():
    return Detection(side="left")


def test_ultrasonic_sensor_detection():
    detection = ultrasonic_sensor_detection()

    assert isinstance(detection, Detection)

    assert isinstance(detection.as_str(), str)
    assert isinstance(detection.as_str(short=True), str)

    assert isinstance(detection.state, DetectionState)
    assert detection.state == DetectionState.CLEAR

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

    assert isinstance(detection.as_image(), np.ndarray)

    assert detection.is_blank is True


# ---


def ultrasonic_sensor_detection_pulse_timeout():
    return Detection(
        side="left",
        detection=False,
        reason="pulse timeout",
    )


def test_ultrasonic_sensor_detection_pulse_timeout():
    detection = ultrasonic_sensor_detection_pulse_timeout()

    assert isinstance(detection.as_str(), str)

    assert detection.state == DetectionState.CLEAR

    assert detection.is_blank is True


# ---


def ultrasonic_sensor_detection_no_echo_high():
    return Detection(
        side="left",
        detection=False,
        reason="no echo high",
    )


def test_ultrasonic_sensor_detection_no_echo_high():
    detection = ultrasonic_sensor_detection_no_echo_high()

    assert isinstance(detection.as_str(), str)

    assert detection.state == DetectionState.CLEAR

    assert detection.is_blank is True


# ---


def ultrasonic_sensor_detection_no_echo_detected():
    return Detection(
        side="left",
        detection=True,
        echo_detected=False,
        pulse_ms=4.0,
        distance_mm=900.0,
    )


def test_ultrasonic_sensor_detection_no_echo_detected():
    detection = ultrasonic_sensor_detection_no_echo_detected()

    assert isinstance(detection.as_str(), str)

    assert detection.state == DetectionState.CLEAR

    assert detection.is_blank is True


# ---


def ultrasonic_sensor_detection_clear():
    return Detection(
        side="left",
        detection=True,
        echo_detected=True,
        pulse_ms=4.0,
        distance_mm=900.0,
    )


def test_ultrasonic_sensor_detection_clear():
    detection = ultrasonic_sensor_detection_clear()

    assert isinstance(detection.as_str(), str)

    assert detection.state == DetectionState.CLEAR

    assert detection.is_blank is False


# ---


def ultrasonic_sensor_detection_warning():
    return Detection(
        side="left",
        detection=True,
        echo_detected=True,
        pulse_ms=4.0,
        distance_mm=300.0,
    )


def test_ultrasonic_sensor_detection_warning():
    detection = ultrasonic_sensor_detection_warning()

    assert isinstance(detection.as_str(), str)

    assert detection.state == DetectionState.WARNING

    assert detection.is_blank is False


# ---


def ultrasonic_sensor_detection_danger():
    return Detection(
        side="left",
        detection=True,
        echo_detected=True,
        pulse_ms=4.0,
        distance_mm=150.0,
    )


def test_ultrasonic_sensor_detection_danger():
    detection = ultrasonic_sensor_detection_danger()

    assert isinstance(detection.as_str(), str)

    assert detection.state == DetectionState.DANGER

    assert detection.is_blank is False

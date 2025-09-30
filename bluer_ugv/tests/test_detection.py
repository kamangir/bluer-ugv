from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import Detection


def test_detection():
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

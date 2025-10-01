import pytest

from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import (
    DetectionState,
)


@pytest.mark.parametrize(
    ["detection_state"],
    [[detection_state] for detection_state in DetectionState],
)
def test_ultrasonic_sensor_detection_state(detection_state: DetectionState):
    color_code = detection_state.color_code
    assert isinstance(color_code, list)
    assert len(color_code) == 3

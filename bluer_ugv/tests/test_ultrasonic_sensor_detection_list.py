import pytest
from typing import Iterable

from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection_list import (
    DetectionList,
)
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import (
    Detection,
    DetectionState,
)
from bluer_ugv.tests.test_ultrasonic_sensor_detection import (
    ultrasonic_sensor_detection_clear,
    ultrasonic_sensor_detection_danger,
    ultrasonic_sensor_detection_warning,
)


@pytest.mark.parametrize(
    [
        "list_of_detections",
        "expected_detection_state",
    ],
    [
        [
            None,
            DetectionState.CLEAR,
        ],
        [
            [
                ultrasonic_sensor_detection_clear(),
                ultrasonic_sensor_detection_danger(),
                ultrasonic_sensor_detection_warning(),
            ],
            DetectionState.DANGER,
        ],
        [
            [
                ultrasonic_sensor_detection_clear(),
                ultrasonic_sensor_detection_warning(),
                ultrasonic_sensor_detection_warning(),
            ],
            DetectionState.WARNING,
        ],
        [
            [
                ultrasonic_sensor_detection_clear(),
                ultrasonic_sensor_detection_clear(),
                ultrasonic_sensor_detection_clear(),
            ],
            DetectionState.CLEAR,
        ],
    ],
)
def test_ultrasonic_sensor_detection_list(
    list_of_detections: Iterable[Detection] | None,
    expected_detection_state: DetectionState,
):
    detection_list = DetectionList(list_of_detections)

    for detection in detection_list:
        assert isinstance(detection, Detection)

    assert isinstance(len(detection_list), int)

    for index in range(len(detection_list)):  # pylint: disable=consider-using-enumerate
        assert isinstance(detection_list[index], Detection)

    detection_list.append(ultrasonic_sensor_detection_clear())

    detection_state = detection_list.state
    assert isinstance(detection_state, DetectionState)
    assert detection_state == expected_detection_state

    for short in [True, False]:
        assert isinstance(detection_list.as_str(short=short), list)
        for item in detection_list.as_str(short=short):
            assert isinstance(item, str)

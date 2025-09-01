import pytest

from bluer_ugv.swallow.session.classical.setpoint.steering import (
    generate_left_and_right,
)

test_cases = [
    [0, 0, 0, 0],
    [0, 50, -50, 50],
    [0, -50, 50, -50],
    [50, 0, 50, 50],
    [-50, 0, -50, -50],
    [50, 50, 0, 100],
    [50, -50, 100, 0],
    [-50, 50, -100, 0],
    [-50, -50, 0, -100],
]


@pytest.mark.parametrize(
    [
        "speed",
        "steering",
        "expected_left",
        "expected_right",
    ],
    test_cases,
)
def test_classical_setpoint_steering(
    speed: int,
    steering: int,
    expected_left: int,
    expected_right: int,
):
    left, right = generate_left_and_right(speed, steering)

    assert left == expected_left
    assert right == expected_right

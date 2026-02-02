import pytest

from bluer_ugv.README.ugvs.location import get_location


# ../../notebooks/ugvs_get_location.ipynb
@pytest.mark.parametrize(
    [
        "hostname",
        "expected_success",
        "expected_location",
    ],
    [
        ["void", False, ""],
        ["swallow2", True, "front"],
        ["sparrow", True, "front"],
        ["sparrow2", True, "front"],
        ["sparrow3-back", True, "back"],
        ["arzhang3-front", True, "front"],
        ["sparrow3-back", True, "back"],
        ["arzhang3-front", True, "front"],
        ["rangin-top2", True, "top"],
    ],
)
def test_ugvs_get_location(
    hostname: str,
    expected_success: bool,
    expected_location: str,
):
    success, location = get_location(hostname)
    assert success == expected_success
    assert location == expected_location

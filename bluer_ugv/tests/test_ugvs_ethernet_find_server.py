import pytest

from bluer_ugv.README.ugvs.ethernet import find_server


# ../../notebooks/ugvs_ethernet_is_server.ipynb
@pytest.mark.parametrize(
    [
        "hostname",
        "expected_success",
        "expected_is_server",
        "expected_server_name",
    ],
    [
        ["void", False, False, ""],
        ["swallow2", True, True, "0.0.0.0"],
        ["sparrow", True, True, "0.0.0.0"],
        ["sparrow2", True, True, "0.0.0.0"],
        ["sparrow3-back", True, False, "sparrow2.local"],
        ["arzhang3-front", True, True, "0.0.0.0"],
        ["sparrow3-back", True, False, "sparrow2.local"],
        ["arzhang3-front", True, True, "0.0.0.0"],
        ["rangin-top2", True, False, "arzhang3-front.local"],
    ],
)
def test_ugvs_ethernet_find_server(
    hostname: str,
    expected_success: bool,
    expected_is_server: bool,
    expected_server_name: str,
):
    success, is_server, server_name_ = find_server(hostname)
    assert success == expected_success
    assert is_server == expected_is_server
    assert server_name_ == expected_server_name

import pytest

from bluer_ugv.swallow.session.classical.config.state import State


@pytest.mark.parametrize(
    ["state"],
    [[detection_state] for detection_state in State],
)
def test_config_state(state: State):
    color_code = state.color_code
    assert isinstance(color_code, list)
    assert len(color_code) == 3

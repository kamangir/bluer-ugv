import pytest
from typing import Dict, Union

from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState


@pytest.mark.parametrize(
    ["params"],
    [
        [
            None,
        ],
        [
            {
                "this": "that",
            }
        ],
    ],
)
def test_scenario_state(
    params: Union[Dict, None],
):
    state = GenericState(params)
    assert state.name
    assert isinstance(state.params, dict)

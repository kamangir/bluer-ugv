import pytest
from typing import Dict, Union

from bluer_ugv.swallow.session.classical.scenario.state.machines.factory import (
    dict_of_state_machines,
)
from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState


@pytest.mark.parametrize(
    ["name"],
    [
        [
            name,
        ]
        for name in dict_of_state_machines.keys()
    ],
)
def test_scenario_state_machine(name: str):
    cls = dict_of_state_machines[name]
    assert cls.name == name

    state_machine = cls()
    assert state_machine.name == name

    for state in state_machine.list_of_states:
        assert isinstance(state, GenericState)

    assert isinstance(state_machine.state, GenericState)

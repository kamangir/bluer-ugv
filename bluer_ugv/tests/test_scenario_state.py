from bluer_ugv.swallow.session.classical.scenario.state.types.generic import State


def test_scenario_state():
    state = State("some name")
    assert state.name
    assert isinstance(state.params, dict)

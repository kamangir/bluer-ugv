from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState


def test_scenario_state():
    state = GenericState("some name")
    assert state.name
    assert isinstance(state.params, dict)

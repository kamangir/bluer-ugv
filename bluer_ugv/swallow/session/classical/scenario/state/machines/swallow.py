from bluer_ugv.swallow.session.classical.scenario.state.machines.generic import (
    GenericStateMachine,
)
from bluer_ugv.swallow.session.classical.scenario.state.starting import StartingState


class SwallowStateMachine(GenericStateMachine):
    name = "swallow"

    def load(self) -> bool:
        self.list_of_states = [
            StartingState(),
        ]

        return super().load()

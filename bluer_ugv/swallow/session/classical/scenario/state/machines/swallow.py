from bluer_ugv.swallow.session.classical.scenario.state.machines.generic import (
    GenericStateMachine,
)
from bluer_ugv.swallow.session.classical.scenario.state.starting import StartingState
from bluer_ugv.logger import logger


class SwallowStateMachine(GenericStateMachine):
    name = "swallow"

    def load(self) -> bool:
        if not super().load():
            return False

        self.list_of_states = [StartingState]
        self.index: int = 0

        return True

from bluer_ugv.swallow.session.classical.scenario.state.machines.generic import (
    GenericStateMachine,
)
from bluer_ugv.swallow.session.classical.scenario.state.approaching import (
    ApproachingState,
)
from bluer_ugv.swallow.session.classical.scenario.state.greeting import (
    GreetingState,
)
from bluer_ugv.swallow.session.classical.scenario.state.listening import (
    ListeningState,
)
from bluer_ugv.swallow.session.classical.scenario.state.responding import (
    RespondingState,
)


class RanginStateMachine(GenericStateMachine):
    name = "rangin"

    def load(self) -> bool:
        self.list_of_states = [
            cls()
            for cls in [
                ApproachingState,
                GreetingState,
                ListeningState,
                RespondingState,
            ]
        ]
        self.index: int = 0

        return super().load()

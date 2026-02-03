from bluer_ugv.swallow.session.classical.keyboard.classes import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.scenario.state.machines.generic import (
    GenericStateMachine,
)
from bluer_ugv.swallow.session.classical.scenario.state.approaching import (
    ApproachingState,
)
from bluer_ugv.swallow.session.classical.scenario.state.speaking import (
    SpeakingState,
)


class RanginStateMachine(GenericStateMachine):
    name = "rangin"

    def load(self) -> bool:
        self.list_of_states = [
            cls(
                keyboard=self.keyboard,
                camera=self.camera,
            )
            for cls in [
                ApproachingState,
                SpeakingState,
            ]
        ]

        return super().load()

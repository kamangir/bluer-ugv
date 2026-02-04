from typing import Tuple

from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState


class SpeakingState(GenericState):
    name: str = "speaking"

    def decide_state_change(self) -> Tuple[bool, str]:
        if not self.config.get("audio_enabled"):
            return True, "approaching"
        return super().decide_state_change()

    def open(self) -> bool:
        self.config.set("audio_enabled", True)
        return super().open()

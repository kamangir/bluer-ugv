from typing import Tuple

from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState


class SpeakingState(GenericState):
    name: str = "speaking"

    def close(self) -> bool:
        self.keyboard.set("audio_enabled", False)
        return super().close()

    def decide_state_change(self) -> Tuple[bool, str]:
        if not self.keyboard.get("audio_enabled"):
            return True, "approaching"
        return super().decide_state_change()

    def open(self) -> bool:
        self.keyboard.set("audio_enabled", True)
        return super().open()

from typing import Dict, Union, Tuple

from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState


class ApproachingState(GenericState):
    name: str = "approaching"

    def __init__(
        self,
        params: Union[Dict, None] = None,
    ):
        super().__init__(params)

    def close(self) -> bool:
        return super().close()

    def decide_state_change(self) -> Tuple[bool, str]:
        return super().decide_state_change()

    def open(self) -> bool:
        return super().open()

    def process(self) -> bool:
        return super().process()

from typing import Tuple
from enum import Enum, auto


class State(Enum):
    CLEAR = auto()
    WARNING = auto()
    DANGER = auto()

    @property
    def color_code(self) -> Tuple[int, int, int]:
        return (
            [0, 255, 0]
            if self == State.CLEAR
            else ([255, 255, 0] if self == State.WARNING else [255, 0, 0])
        )

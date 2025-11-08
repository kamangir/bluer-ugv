from enum import Enum

from bluer_ugv.README.ugvs.comparison.features.classes import Feature


class UGV_Control(Enum):
    AI = 2
    RC = 1


class ControlFeature(Feature):
    nickname = "control"

    def __init__(
        self,
        score: UGV_Control,
    ):
        super().__init__(
            score=score,
            better_func=lambda score_1, score_2: score_1.score > score_2.score,
        )

    def brag(self) -> str:
        return "سامانه‌ی هوش مصنوعی"

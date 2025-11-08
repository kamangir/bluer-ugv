from enum import Enum

from bluer_ugv.README.ugvs.comparison.features.classes import Feature


class UGV_Size(Enum):
    SMALL = 100
    MEDIUM = 10
    LARGE = 1


class SizeFeature(Feature):
    nickname = "size"

    def __init__(
        self,
        score: UGV_Size,
    ):
        super().__init__(
            score=score,
            better_func=lambda score_1, score_2: score_1.score < score_2.score,
        )

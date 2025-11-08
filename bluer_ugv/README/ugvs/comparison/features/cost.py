from enum import Enum

from bluer_ugv.README.ugvs.comparison.features.classes import Feature


class UGV_Cost(Enum):
    LOW = 100  # < 50 mT ~= $500
    MEDIUM = 10  # < 500 mT ~= $5k
    HIGH = 1  # < 5 MT ~= $50k


class CostFeature(Feature):
    nickname = "cost"

    def __init__(
        self,
        score: UGV_Cost,
    ):
        super().__init__(
            score=score,
            better_func=lambda score_1, score_2: score_1.score < score_2.score,
        )

    def brag(
        self,
        ugv_name: str,
    ) -> str:
        return f"قیمت پایین‌تر {ugv_name}"

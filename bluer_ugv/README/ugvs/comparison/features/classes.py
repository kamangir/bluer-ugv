from typing import Dict, Callable


class Feature:
    nickname: str

    def __init__(
        self,
        score: int = -1,
        better_func: Callable = lambda score_1, score_2: score_1 > score_2,
    ):
        self.score = score
        self.better_func = better_func

    def brag(
        self,
        ugv_name: str,
    ) -> str:
        return f"{ugv_name} {self.nickname}: {self.score}"


class FeatureList:
    def __init__(self):
        self.db: Dict[Feature] = {}

    def add(self, feature: Feature):
        self.db[feature] = False

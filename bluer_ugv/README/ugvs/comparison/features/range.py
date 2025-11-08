from bluer_ugv.README.ugvs.comparison.features.classes import Feature

unlimited_range: int = 999


class RangeFeature(Feature):
    nickname = "range"

    def __init__(
        self,
        score: float,  # km, 999: unlimited
    ):
        super().__init__(
            score=score,
            better_func=lambda score_1, score_2: score_1 > score_2,
        )

    def brag(self) -> str:
        return "شعاع عملکرد عملیاتی {}".format(
            "نامحدود" if self.score == -1 else f"{self.score} کیلومتر"
        )

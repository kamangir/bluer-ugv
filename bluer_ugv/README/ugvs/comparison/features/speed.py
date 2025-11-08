from bluer_ugv.README.ugvs.comparison.features.classes import Feature


class SpeedFeature(Feature):
    nickname = "speed"

    def __init__(
        self,
        score: float,  # km/h
    ):
        super().__init__(
            score=score,
            better_func=lambda score_1, score_2: score_1 > score_2,
        )

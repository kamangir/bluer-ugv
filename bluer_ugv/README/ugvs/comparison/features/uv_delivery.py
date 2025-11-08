from bluer_ugv.README.ugvs.comparison.features.classes import Feature


class UVDeliveryFeature(Feature):
    nickname = "uv_delivery"

    def __init__(
        self,
        score: bool,
    ):
        super().__init__(
            score=score,
            better_func=lambda score_1, score_2: score_1 and not score_2,
        )

    def brag(self) -> str:
        return "حمل پهپاد و رهپاد"

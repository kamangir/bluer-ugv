from bluer_ugv.README.ugvs.comparison.features.classes import Feature


class SanctionProofFeature(Feature):
    nickname = "sanction_proof"

    def __init__(
        self,
        score: bool,
    ):
        super().__init__(
            score=score,
            better_func=lambda score_1, score_2: score_1 and not score_2,
        )

    def brag(
        self,
        ugv_name: str,
    ) -> str:
        return f"تحریم گریزی {ugv_name}"

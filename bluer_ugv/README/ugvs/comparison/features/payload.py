from bluer_ugv.README.ugvs.comparison.features.classes import (
    Feature,
    Feature_Comparison,
)


class PayloadFeature(Feature):
    nickname = "payload"
    long_name = "توان حمل بار"

    comparison_as_str = {
        Feature_Comparison.HIGHER: "بیشتر",
        Feature_Comparison.LOWER: "کمتر",
        Feature_Comparison.SIMILAR: "مشابه",
    }

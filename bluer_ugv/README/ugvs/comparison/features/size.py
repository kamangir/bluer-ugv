from enum import Enum

from bluer_ugv.README.ugvs.comparison.features.classes import (
    Feature,
    Feature_Comparison,
)


class UGV_Size(Enum):
    SMALL = 100
    MEDIUM = 10
    LARGE = 1


class SizeFeature(Feature):
    nickname = "size"
    long_name = "اندازه"

    comparison_as_str = {
        Feature_Comparison.HIGHER: "کوچکتر",
        Feature_Comparison.LOWER: "بزرگتر",
        Feature_Comparison.SIMILAR: "مشابه",
    }

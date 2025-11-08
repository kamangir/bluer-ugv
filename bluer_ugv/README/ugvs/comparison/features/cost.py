from enum import Enum

from bluer_ugv.README.ugvs.comparison.features.classes import (
    Feature,
    Feature_Comparison,
)


class UGV_Cost(Enum):
    LOW = 100  # < 50 mT ~= $500
    MEDIUM = 10  # < 500 mT ~= $5k
    HIGH = 1  # < 5 MT ~= $50k


class CostFeature(Feature):
    nickname = "cost"
    long_name = "هزینه"

    comparison_as_str = {
        Feature_Comparison.HIGHER: "پایین‌تر",
        Feature_Comparison.LOWER: "بالاتر",
        Feature_Comparison.SIMILAR: "مشابه",
    }

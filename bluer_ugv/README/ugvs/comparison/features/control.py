from enum import Enum

from bluer_ugv.README.ugvs.comparison.features.classes import Feature


class UGV_Control(Enum):
    AI = 2
    RC = 1


class ControlFeature(Feature):
    nickname = "control"
    long_name = "سامانه‌ی هوش مصنوعی"

    comparison_as_str = {}

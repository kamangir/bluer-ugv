from typing import List, Any, Union, Tuple, Dict
from enum import Enum, auto


class Feature_Comparison(Enum):
    SIMILAR = auto()
    HIGHER = auto()
    LOWER = auto()


class Feature:
    nickname: str
    long_name: str

    description_template = "{} در {} {} {} ({})"
    both_template = "هر دو"

    comparison_as_str: Dict[Feature_Comparison, str] = {
        Feature_Comparison.HIGHER: "بیشتر",
        Feature_Comparison.LOWER: "کمتر",
        Feature_Comparison.SIMILAR: "مشابه",
    }

    def __init__(
        self,
        score: Any,
    ):
        self.score = score

    def compare(
        self,
        feature: Union["Feature", None],
        ugv_name_1: str,
        ugv_name_2: str,
        ugv_name_both: str = both_template,
    ) -> Tuple[Feature_Comparison, str]:
        status: Feature_Comparison = Feature_Comparison.HIGHER
        if feature is not None:
            if self.score_index == feature.score_index:
                status = Feature_Comparison.SIMILAR
            elif self.score_index < feature.score_index:
                status = Feature_Comparison.LOWER

        return status, self.describe(
            status,
            ugv_name_1,
            ugv_name_2,
            ugv_name_both,
        )

    def describe(
        self,
        status: Feature_Comparison,
        ugv_name_1: str,
        ugv_name_2: str,
        ugv_name_both: str,
    ) -> str:
        return self.description_template.format(
            self.__class__.comparison_as_str.get(status, ""),
            self.long_name,
            status.name,
            self.score,
            (
                ugv_name_1
                if status == Feature_Comparison.HIGHER
                else ugv_name_2 if status == Feature_Comparison.LOWER else ugv_name_both
            ),
        )

    @property
    def score_index(self):
        return (
            int(self.score)
            if isinstance(self.score, bool)
            else self.score.value if isinstance(self.score, Enum) else self.score
        )


class FeatureList:
    def __init__(self):
        self.db: List[Feature] = []

    def add(self, feature: Feature):
        self.db.append(feature)

    def get(
        self,
        feature_name: str,
    ) -> Union[Feature, None]:
        for feature in self.db:
            if feature_name == feature.nickname:
                return feature

        return None

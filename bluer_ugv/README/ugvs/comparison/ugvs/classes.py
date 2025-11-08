from typing import List, Dict, Any

from bluer_ugv.README.ugvs.comparison.features.classes import FeatureList
from bluer_ugv.README.ugvs.comparison.ugvs.features import dict_of_feature_classes
from bluer_ugv.logger import logger


class UGV:
    def __init__(
        self,
        nickname: str,
        name: str,
        features: Dict[str:Any],
        deficiencies: List[str] = [],
    ):
        self.nickname = nickname
        self.name = name

        self.feature_list: FeatureList = FeatureList()

        for feature_name, feature_value in features.items():
            if feature_name not in dict_of_feature_classes:
                logger.error(f"{feature_name} not found.")
                assert False

            self.feature_list.add(dict_of_feature_classes[feature_name](feature_value))

        self.deficiencies = deficiencies


class List_of_UGVs:
    def __init__(self):
        self.db: List[UGV] = []

    def add(
        self,
        **kw_args,
    ):
        ugv = UGV(**kw_args)
        self.db.append(ugv)

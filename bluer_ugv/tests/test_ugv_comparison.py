from bluer_ugv.README.ugvs.comparison.features.db import list_of_feature_classes
from bluer_ugv.README.ugvs.comparison.references.db import list_of_references
from bluer_ugv.README.ugvs.comparison.ugvs.db import list_of_ugvs
from bluer_ugv.README.ugvs.comparison.ugvs.classes import UGV
from bluer_ugv.README.ugvs.comparison.build import build


def test_ugv_comparison_build():
    assert build()


def test_ugv_comparison_list_of_feature_classes():
    for feature_class_1 in list_of_feature_classes:
        assert feature_class_1.long_name

        for feature_class_2 in list_of_feature_classes:
            if feature_class_1 != feature_class_2:
                assert (
                    feature_class_1.nickname != feature_class_2.nickname
                ), f"{feature_class_1}.nickname == {feature_class_2}.nickname"


def test_ugv_comparison_list_of_references():
    for reference in list_of_references.db:
        for ugv_name in reference.list_of_ugvs:
            assert any(
                ugv_name == ugv.nickname for ugv in list_of_ugvs.db
            ), f"{ugv_name}: ugv not found."


def test_ugv_comparison_list_of_ugvs():
    for ugv in list_of_ugvs.db:
        assert isinstance(ugv, UGV)

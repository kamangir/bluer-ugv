from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_ugv import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_ugv_env():
    assert env.BLUER_BEAST_MODEL

    assert isinstance(env.BLUER_UGV_CAMERA_TRAINING_PERIOD, float)
    assert env.BLUER_UGV_CAMERA_TRAINING_PERIOD > 0

    assert isinstance(env.BLUER_UGV_CAMERA_PREDICTION_PERIOD, float)
    assert env.BLUER_UGV_CAMERA_PREDICTION_PERIOD > 0

    assert isinstance(env.BLUER_UGV_MOUSEPAD_ENABLED, int)

    assert isinstance(env.BLUER_UGV_SWALLOW_DATASET_LIST, str)
    assert env.BLUER_UGV_SWALLOW_DATASET_LIST

    assert isinstance(env.BLUER_UGV_SWALLOW_MODEL, str)
    assert env.BLUER_UGV_SWALLOW_MODEL

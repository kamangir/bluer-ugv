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

    assert isinstance(env.BLUER_UGV_CAMERA_ACTION_PERIOD, float)
    assert env.BLUER_UGV_CAMERA_ACTION_PERIOD > 0

    assert isinstance(env.BLUER_UGV_SWALLOW_STEERING_SETPOINT, int)
    assert env.BLUER_UGV_SWALLOW_STEERING_SETPOINT > 0

    assert isinstance(env.BLUER_UGV_MOUSEPAD_ENABLED, int)

    for object_name in [
        env.BLUER_UGV_SWALLOW_NAVIGATION_DATASET_LIST,
        env.BLUER_UGV_SWALLOW_NAVIGATION_MODEL,
        env.BLUER_UGV_SWALLOW_YOLO_DATASET_LIST,
        env.BLUER_UGV_SWALLOW_YOLO_MODEL,
    ]:
        assert isinstance(object_name, str)
        assert object_name

    assert isinstance(env.BLUER_UGV_ULTRASONIC_SENSOR_TEST_OBJECT, str)

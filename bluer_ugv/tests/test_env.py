from bluer_options.testing import (
    are_01,
    are_positive_floats,
    are_positive_ints,
    are_nonempty_strs,
)
from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_ugv import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_ugv_env():
    assert are_positive_floats(
        [
            env.BLUER_UGV_CAMERA_ACTION_PERIOD,
            env.BLUER_UGV_CAMERA_TRAINING_PERIOD,
            env.BLUER_UGV_SWALLOW_STEERING_YOLO_EXPIRY,
            env.BLUER_UGV_ULTRASONIC_SENSOR_DANGER_THRESHOLD,
            env.BLUER_UGV_ULTRASONIC_SENSOR_WARNING_THRESHOLD,
        ]
    )

    assert are_positive_ints(
        [
            env.BLUER_UGV_AUDIO_CHANNELS,
            env.BLUER_UGV_AUDIO_LENGTH,
            env.BLUER_UGV_AUDIO_RATE,
            env.BLUER_UGV_ETHERNET_PORT,
            env.BLUER_UGV_SWALLOW_STEERING_SETPOINT,
        ]
    )

    assert are_nonempty_strs(
        [
            env.BLUER_UGV_AUDIO_LANGUAGE,
            env.BLUER_UGV_BEAST_MODEL,
            env.BLUER_UGV_RELEASE_2,
            env.BLUER_UGV_SWALLOW_NAVIGATION_DATASET_LIST,
            env.BLUER_UGV_SWALLOW_NAVIGATION_MODEL,
            env.BLUER_UGV_SWALLOW_YOLO_DATASET_LIST,
            env.BLUER_UGV_SWALLOW_YOLO_MODEL,
            env.BLUER_UGV_ULTRASONIC_SENSOR_TEST_OBJECT,
            env.RANGIN_VIDEO_LIST_OBJECT,
        ]
    )

    assert are_01(
        [
            env.BLUER_UGV_MOUSEPAD_ENABLED,
            env.BLUER_UGV_ULTRASONIC_SENSOR_ENABLED,
            env.BLUER_UGV_ULTRASONIC_SENSOR_ENABLED,
            env.BLUER_UGV_ULTRASONIC_SENSOR_KEEP_LOG,
            env.BLUER_UGV_ULTRASONIC_SENSOR_LOG,
        ]
    )

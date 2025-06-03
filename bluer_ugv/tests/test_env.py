from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_ugv import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_ugv_env():
    assert env.BLUER_BEAST_MODEL

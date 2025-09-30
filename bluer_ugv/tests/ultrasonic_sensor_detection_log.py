import pytest

from blueness import module
from bluer_objects import storage
from bluer_objects.storage.policies import DownloadPolicy

from bluer_ugv import NAME
from bluer_ugv import env
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


@pytest.fixture
def test_object():
    object_name = env.BLUER_UGV_ULTRASONIC_SENSOR_TEST_OBJECT

    assert storage.download(
        object_name=object_name,
        policy=DownloadPolicy.DOESNT_EXIST,
    )

    yield object_name

    logger.info(f"deleting {NAME}.test_object ...")

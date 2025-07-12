from blueness import module

from bluer_ugv import NAME
from bluer_ugv.swallow.dataset.dataset import ImageDataset
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def review(object_name: str) -> bool:
    logger.info(f"{NAME}.review({object_name})")

    success, _ = ImageDataset.load(object_name=object_name)

    return success

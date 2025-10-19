from blueness import module

from bluer_ugv import NAME
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


def test(keys: str = "") -> bool:
    logger.info("{}.testing({})".format(NAME, keys))

    logger.info("🪄")

    return True

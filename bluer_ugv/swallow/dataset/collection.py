from blueness import module

from bluer_ugv import NAME
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


def collect(
    object_name: str,
    count: int = -1,
    update_metadata=False,
) -> bool:
    logger.info(
        "{}.collect({}{}) -> {}".format(
            NAME,
            "all" if count == -1 else f"count={count}",
            ",update_metadata" if update_metadata else "",
            object_name,
        )
    )

    logger.info("🪄")

    return True

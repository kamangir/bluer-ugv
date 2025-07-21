from typing import Dict, List, Tuple

from blueness import module

from bluer_ugv import NAME
from bluer_ugv.parts.db import db_of_parts
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


def get_list_of_parts(
    dict_of_parts: Dict[str, str],
    reference: str = "../../parts",
) -> Tuple[bool, List[str]]:
    logger.info(
        "{}.get_list_of_parts: {}".format(
            NAME,
            ", ".join(dict_of_parts.keys()),
        )
    )

    for part_name in dict_of_parts:
        if part_name not in db_of_parts:
            logger.error(f"{part_name}: part not found.")
            return False, []

    return True, sorted(
        [
            (
                "1. [{}{}]({}).".format(
                    db_of_parts[part_name][0],
                    ": {}".format(description) if description else "",
                    f"{reference}/{part_name}.md",
                )
            )
            for part_name, description in dict_of_parts.items()
        ]
    )

import os
from typing import List, Union
from functools import reduce

from blueness import module
from bluer_objects import file

from bluer_ugv import NAME
from bluer_ugv.README.ugvs.comparison.ugvs.db import list_of_ugvs
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def build(
    log: bool = True,
    reference_ugv_name: str = "arzhang",
) -> bool:
    reference_ugv = list_of_ugvs.get(reference_ugv_name)
    if reference_ugv is None:
        logger.error(f"{reference_ugv_name}: reference ugv not found.")
        return False

    logger.info(f"{NAME}.build")

    success, contents = file.load_text(
        file.absolute(
            "../../../assets/comparison.html",
            reference_path=file.path(__file__),
        ),
        log=log,
    )
    if not success:
        return success

    try:
        content_index = [line.strip() for line in contents].index("contents:::")
    except Exception as e:
        logger.error(f"contents::: not found: {e}")
        return False

    contents = (
        contents[:content_index]
        + row_of(
            [
                "رديف",
                "نام محصول مشابه",
                "مشابهت و تفاوت ها محصول شما با آنها ",
            ],
            header=True,
        )
        + reduce(
            lambda x, y: x + y,
            [
                row_of(
                    [
                        str(index + 1),
                        ugv.description,
                        reference_ugv.compare(ugv),
                    ]
                )
                for index, ugv in enumerate(
                    [
                        ugv_
                        for ugv_ in list_of_ugvs.db
                        if ugv_.nickname not in [reference_ugv_name, "template"]
                    ]
                )
            ],
            [],
        )
        + contents[content_index + 1 :]
    )

    return file.save_text(
        file.absolute(
            "../../../docs/UGVs/comparison.html",
            reference_path=file.path(__file__),
        ),
        contents,
        log=log,
    )


def row_of(
    row: Union[List[str], List[List[str]]],
    header: bool = False,
) -> List[str]:
    return (
        ["{}<tr>".format(8 * "")]
        + reduce(
            lambda x, y: x + y,
            [
                [
                    "{}<{}>".format(
                        12 * " ",
                        "th" if header else "td",
                    )
                ]
                + ([item] if isinstance(item, str) else list(item))
                + [
                    "</{}>".format(
                        "th" if header else "td",
                    )
                ]
                for item in row
            ],
            [],
        )
        + ["{}</tr>".format(8 * "")]
    )

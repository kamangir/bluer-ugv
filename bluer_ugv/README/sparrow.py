from bluer_objects.README.items import ImageItems

from bluer_ugv.parts.db import db_of_parts
from bluer_ugv.sparrow.README import items
from bluer_ugv.sparrow.parts import dict_of_parts
from bluer_ugv.README.consts import algo_docs, assets2_bluer_swallow

docs = [
    {
        "items": items,
        "path": "../docs/bluer_sparrow",
        "cols": 2,
    },
    {"path": "../docs/bluer_sparrow/design"},
    {"path": "../docs/bluer_sparrow/design/specs.md"},
    {
        "path": "../docs/bluer_sparrow/design/parts.md",
        "items": db_of_parts.as_images(
            dict_of_parts,
            reference="../../parts",
        ),
        "macros": {
            "parts:::": db_of_parts.as_list(
                dict_of_parts,
                reference="../../parts",
                log=False,
            ),
        },
    },
    {
        "path": "../docs/bluer_sparrow/algo",
    },
    {
        "path": "../docs/bluer_sparrow/algo/target-detection",
        "items": ImageItems(
            {
                f"{assets2_bluer_swallow}/target-selection.png": f"{algo_docs}/socket.md",
            }
        ),
    },
]

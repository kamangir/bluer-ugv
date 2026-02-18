from bluer_sbc.parts.db import db_of_parts

from bluer_ugv.designs.swallow.parts import dict_of_parts

docs = [
    {
        "path": "../docs/swallow/digital/design/parts.md",
        "items": db_of_parts.as_images(
            dict_of_parts,
            reference="repo",
        ),
        "macros": {
            "parts:::": db_of_parts.as_list(
                dict_of_parts,
                reference="repo",
                log=False,
            ),
        },
    },
]

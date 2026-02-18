from bluer_sbc.parts.db import db_of_parts

from bluer_ugv.README.swallow.digital.design.arzhang4 import tagline, v1
from bluer_ugv.designs.swallow.parts import dict_of_parts

docs = [
    {
        "path": "../docs/swallow/digital/design/arzhang4",
        "items": db_of_parts.as_images(
            dict_of_parts,
            reference="repo",
        ),
        "macros": {
            "tagline:::": tagline,
            "parts:::": db_of_parts.as_list(
                dict_of_parts,
                reference="repo",
                log=False,
            ),
        },
    },
] + v1.docs

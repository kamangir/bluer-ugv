from bluer_sbc.parts.db import db_of_parts
from bluer_sbc.README.design import design_doc_parts

from bluer_ugv.README.swallow.digital.design.arzhang4 import tagline, v1
from bluer_ugv.designs.swallow.parts import dict_of_parts

docs = [
    {
        "path": "../docs/swallow/digital/design/arzhang4",
        "macros": {
            **design_doc_parts(
                dict_of_parts=dict_of_parts,
                parts_reference="repo",
            ),
            "tagline:::": tagline,
        },
    },
] + v1.docs

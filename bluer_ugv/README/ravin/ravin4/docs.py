from bluer_ugv.README.ravin.ravin4.consts import description
from bluer_ugv.README.ravin.ravin4.items import items
from bluer_ugv.README.ravin.ravin4 import build, body, packaging, parts, schematics

docs = (
    [
        {
            "items": items,
            "path": "../docs/ravin/ravin4",
            "macros": {
                "description:::": [description],
            },
        },
    ]
    + build.docs
    + body.docs
    + packaging.docs
    + parts.docs
    + schematics.docs
)

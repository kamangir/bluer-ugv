from bluer_sbc.parts.db import db_of_parts

dict_of_parts = {
    "brushless-driver": "4 x",
    "dc-circuit-breaker": "40 A",
    "dsn-vc288": "with 50 A shunt",
    "scooter-wheel": "4 x",
    "SLA-Battery": "12 V, 42 Ah, 185 mm x 150 mm x 175 mm",
}

docs = [
    {
        "path": "../docs/swallow/digital/design/arzhang4/part-selection.md",
    },
    {
        "path": "../docs/swallow/digital/design/arzhang4/parts.md",
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

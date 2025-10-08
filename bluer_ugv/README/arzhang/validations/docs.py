from bluer_objects.README import Items

from bluer_ugv.README.arzhang.validations.db import validations

docs = [
    {
        "path": "../docs/arzhang/validation",
        "items": Items(
            [
                {
                    "name": validation_name,
                    "marquee": info["marquee"],
                    "url": f"./{validation_name}.md",
                }
                for validation_name, info in validations.items()
                if validation_name != "template" and "marquee" in info
            ]
        ),
        "macros": {
            "list:::": [
                f"- [{validation_name}](./{validation_name}.md)"
                for validation_name in validations
                if validation_name != "template"
            ]
        },
        "cols": 2,
    }
] + [
    {
        "path": f"../docs/arzhang/validation/{validation_name}.md",
        "items": info.get("items", []),
        "macros": {
            **info.get("macros", {}),
            "ugv_name:::": [
                "UGV: [`{ugv_name}`](../../UGVs/{ugv_name}.md)".format(
                    ugv_name=info.get(
                        "ugv_name",
                        "unknown",
                    )
                )
            ],
        },
        "cols": info.get("cols", 3),
    }
    for validation_name, info in validations.items()
    if validation_name != "template"
]

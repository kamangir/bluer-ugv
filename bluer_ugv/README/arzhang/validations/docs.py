from bluer_ugv.README.arzhang.validations.db import validations

docs = [
    {
        "path": "../docs/arzhang/validation",
        "macros": {
            "list:::": [
                f"- [{validation_name}](./{validation_name}.md)"
                for validation_name in validations
                if validation_name != "template"
            ]
        },
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

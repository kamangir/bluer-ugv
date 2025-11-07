from bluer_objects.README.items import Items_of_dict, list_of_dict

from bluer_ugv.README.arzhang.validations.db import dict_of_validations
from bluer_ugv import ICON

docs = [
    {
        "path": "../docs/arzhang/validation",
        "items": Items_of_dict(dict_of_validations),
        "macros": {
            "list:::": list_of_dict(dict_of_validations),
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
                "UGV(s): {}".format(
                    ", ".join(
                        [
                            "{icon} [`{ugv_name}`](../../UGVs/{ugv_name}.md)".format(
                                icon=(
                                    (
                                        lambda keyword: (
                                            "⚓️"
                                            if keyword == "anchor"
                                            else (
                                                ICON
                                                if keyword == "ugv"
                                                else "❓ keyword"
                                            )
                                        )
                                    )(ugv_name.split(":")[1])
                                    if ":" in ugv_name
                                    else ICON
                                ),
                                ugv_name=ugv_name.split(":")[0],
                            )
                            for ugv_name in (
                                lambda thing: (
                                    thing
                                    if isinstance(thing, list)
                                    else thing.split(",")
                                )
                            )(
                                info.get(
                                    "ugv_name",
                                    ["unknown"],
                                )
                            )
                        ]
                    )
                )
            ],
        },
        "cols": info.get("cols", 3),
    }
    for validation_name, info in dict_of_validations.items()
    if validation_name != "template"
]

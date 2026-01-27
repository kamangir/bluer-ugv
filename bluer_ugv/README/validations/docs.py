from bluer_objects.README.items import Items_of_dict, list_of_dict

from bluer_ugv.README.validations.db import dict_of_validations
from bluer_ugv import ICON

docs = [
    {
        "path": "../docs/validations",
        "items": Items_of_dict(dict_of_validations),
        "macros": {
            "list:::": list_of_dict(dict_of_validations),
        },
        "cols": 4,
    }
] + [
    {
        "path": f"../docs/validations/{validation_name}.md",
        "items": info.get("items", []),
        "macros": {
            **info.get("macros", {}),
            "ugv_name:::": [
                "UGV(s): {}".format(
                    ", ".join(
                        [
                            "{icon} [`{ugv_name}`](../UGVs/{ugv_name}.md)".format(
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
                                ugv_name=ugv_name.split(":", 1)[0],
                            )
                            for ugv_name in info["ugv_name"]
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

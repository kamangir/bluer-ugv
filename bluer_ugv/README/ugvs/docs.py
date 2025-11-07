from bluer_objects.README.items import ImageItems

from bluer_ugv.README.ugvs.db import dict_of_ugvs


docs = [
    {
        "path": f"../docs/UGVs/{ugv_name}.md",
        "items": ImageItems({item: "" for item in info.get("items", [])}),
        "macros": {
            "validations:::": [
                "validations: TBA",
            ]
        },
    }
    for ugv_name, info in dict_of_ugvs.items()
]

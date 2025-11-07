from bluer_ugv.README.ugvs.db import dict_of_ugvs


docs = [
    {
        "path": f"../docs/UGVs/{ugv_name}.md",
        "items": info.get("items", []),
        "macros": {
            "validations:::": [
                "validations: TBA",
            ]
        },
    }
    for ugv_name, info in dict_of_ugvs.items()
]

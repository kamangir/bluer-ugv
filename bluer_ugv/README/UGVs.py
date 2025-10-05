from bluer_objects.README.items import ImageItems

from bluer_ugv.README.consts import (
    assets2_arzhang,
    assets2_bluer_swallow,
    assets2_bluer_ugv,
)

docs = [
    {
        "path": "../docs/UGVs",
    },
    {
        "path": "../docs/UGVs/swallow.md",
        "items": ImageItems(
            {
                f"{assets2_bluer_swallow}/20250701_2206342_1.gif": "",
                f"{assets2_bluer_swallow}/20250913_203635~2_1.gif": "",
            }
        ),
    },
    {
        "path": "../docs/UGVs/arzhang.md",
        "items": ImageItems(
            {
                f"{assets2_arzhang}/VID-20250905-WA0014_1.gif": "",
                f"{assets2_arzhang}/20251005_112530.jpg": "",
            }
        ),
    },
    {
        "path": "../docs/UGVs/arzhang2.md",
        "items": ImageItems(
            {
                f"{assets2_arzhang}/VID-20250905-WA0014_1.gif": "",
            }
        ),
    },
    {
        "path": "../docs/UGVs/arzhang3.md",
        "items": ImageItems({f"{assets2_bluer_ugv}/bluer-light.png": ""}),
    },
    {
        "path": "../docs/UGVs/rangin.md",
        "items": ImageItems(
            {
                "https://github.com/kamangir/assets/blob/main/bluer-ugv/bluer-light.png": ""
            }
        ),
    },
]

from bluer_objects.README.items import ImageItems, Items
from bluer_objects import markdown

from bluer_ugv.README.consts import (
    assets2_swallow,
    assets2_bluer_ugv,
    swallow_electrical_design,
)

items = markdown.generate_table(
    Items(
        [
            {
                "name": "parts",
                "url": "./bluer_ugv/docs/swallow/digital/design/parts.md",
                "marquee": f"{assets2_bluer_ugv}/XL4015.png",
            },
            {
                "name": "shield",
                "url": "./bluer_ugv/docs/swallow/digital/design/shield.md",
                "marquee": f"{swallow_electrical_design}/digital.png?raw=true",
            },
            {
                "name": "terraform",
                "url": "./bluer_ugv/docs/swallow/digital/design/terraform.md",
                "marquee": f"{assets2_swallow}/20250611_100917.jpg?raw=true",
            },
            {
                "name": "UGVs",
                "url": "./bluer_ugv/docs/UGVs",
                "marquee": f"{assets2_swallow}/20250912_211652.jpg?raw=true",
            },
        ]
    ),
    cols=4,
)

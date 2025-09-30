from bluer_objects.README.items import ImageItems, Items
from bluer_objects import markdown

from bluer_ugv.README.consts import (
    bluer_swallow_mechanical_design,
    assets2_bluer_ugv,
    assets2_bluer_swallow,
)

items = markdown.generate_table(
    Items(
        [
            {
                "name": "parts",
                "url": "./bluer_ugv/docs/bluer_swallow/digital/design/parts.md",
                "marquee": f"{assets2_bluer_ugv}/XL4015.png",
            },
            {
                "name": "shield",
                "url": "./bluer_ugv/docs/bluer_swallow/digital/design/shield.md",
                "marquee": f"{bluer_swallow_mechanical_design}/electrical/digital.png?raw=true",
            },
            {
                "name": "terraform",
                "url": "./bluer_ugv/docs/bluer_swallow/digital/design/terraform.md",
                "marquee": f"{assets2_bluer_swallow}/20250611_100917.jpg?raw=true",
            },
        ]
    )
)

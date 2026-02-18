from bluer_objects.README.items import ImageItems

from bluer_ugv.README.swallow.consts import swallow_assets2
from bluer_ugv.swallow.session.classical.controller.keyboard.keys import ControlKeys


docs = [
    {
        "path": "../docs/swallow/digital/design/operation.md",
        "cols": 2,
        "items": ImageItems(
            {
                f"{swallow_assets2}/20251019_121811.jpg": "",
                f"{swallow_assets2}/20251019_121842.jpg": "",
            }
        ),
        "macros": {
            "keys:::": ControlKeys.as_table(),
        },
    },
]

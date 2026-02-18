from bluer_objects.README.items import ImageItems

from bluer_ugv.README.swallow.consts import swallow_electrical_designs

docs = [
    {
        "path": "../docs/swallow/digital/design/steering-over-current-detection.md",
        "items": ImageItems(
            {
                f"{swallow_electrical_designs}/steering-over-current.png": f"{swallow_electrical_designs}/steering-over-current.svg",
            }
        ),
    },
]

from bluer_objects.README.consts import designs_url
from bluer_objects.README.items import ImageItems


docs = [
    {
        "path": f"../docs/swallow/digital/design/joystick{suffix}",
        "items": ImageItems(items),
    }
    for suffix, items in {
        "": {},
        "/validation.md": {},
        "/operation.md": {
            designs_url(
                "swallow/joystick/controls.png",
            ): designs_url(
                "swallow/joystick/controls.svg",
            )
        },
    }.items()
]

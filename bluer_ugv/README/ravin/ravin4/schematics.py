from bluer_objects.README.items import ImageItems

from bluer_ugv.README.ravin.ravin4.consts import designs

docs = [
    {
        "path": "../docs/ravin/ravin4/schematics.md",
        "items": ImageItems(
            {
                f"{designs}/wiring.png": f"{designs}/wiring.svg",
            }
        ),
    },
]

from bluer_objects.README.items import ImageItems

from bluer_ugv.README.swallow.consts import swallow_designs


items = ImageItems(
    {
        f"{swallow_designs}/kicad/swallow/exports/swallow.png": f"{swallow_designs}/kicad/swallow/exports/swallow.pdf",
        f"{swallow_designs}/kicad/swallow/exports/swallow-3d.png": "",
        f"{swallow_designs}/kicad/swallow/exports/swallow-3d-back.png": "",
        f"{swallow_designs}/kicad/swallow/exports/swallow-pcb.png": "",
    }
)

docs = [
    {
        "path": "../docs/swallow/digital/design/shield/pcb.md",
        "items": items,
    },
]

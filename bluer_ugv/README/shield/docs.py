from bluer_objects.README.items import ImageItems

from bluer_ugv.README.swallow.consts import (
    swallow_assets2,
    swallow_designs,
    swallow_electrical_designs,
)
from bluer_ugv.README.shield import pcb, schematics, testing

items = ImageItems(
    {
        f"{swallow_assets2}/20250614_102301.jpg": "",
        f"{swallow_assets2}/20250703_153834.jpg": "",
        f"{swallow_assets2}/20250925_213013.jpg": "",
        f"{swallow_assets2}/20250925_214017.jpg": "",
        f"{swallow_assets2}/20250928_160425.jpg": "",
        f"{swallow_assets2}/20250928_160449.jpg": "",
        f"{swallow_assets2}/20251002_103712.jpg": "",
        f"{swallow_assets2}/20251002_103720.jpg": "",
        f"{swallow_electrical_designs}/nuts-bolts-spacers.png": f"{swallow_electrical_designs}/nuts-bolts-spacers.svg",
        f"{swallow_assets2}/20251018_133202.jpg": "",
        f"{swallow_assets2}/20251018_133349.jpg": "",
        f"{swallow_assets2}/20251008_114557.jpg": "",
        f"{swallow_assets2}/20251008_133418.jpg": "",
        f"{swallow_assets2}/20251008_124129.jpg": "",
        f"{swallow_assets2}/20251008_124932.jpg": "",
        f"{swallow_assets2}/20251112_085331.jpg": "",
        f"{swallow_assets2}/20251112_181047.jpg": "",
        f"{swallow_assets2}/20251112_181053.jpg": "",
    }
)


docs = (
    [
        {
            "path": "../docs/swallow/digital/design/shield",
            "items": items,
        },
    ]
    + pcb.docs
    + schematics.docs
    + testing.docs
)

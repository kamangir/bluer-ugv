from bluer_objects.README.items import Items

from bluer_ugv.README.ravin.ravin3 import consts as ravin3
from bluer_ugv.README.ravin.ravin4 import consts as ravin4


items = Items(
    [
        {
            "name": "ravin3",
            "description": ravin3.description,
            "marquee": f"{ravin3.assets}/TBA.jpg",
            "url": "./ravin3",
        },
        {
            "name": "ravin4",
            "description": ravin4.description,
            "marquee": f"{ravin4.assets}/TBA.jpg",
            "url": "./ravin4",
        },
    ]
)

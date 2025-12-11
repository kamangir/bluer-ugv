from bluer_objects.README.items import ImageItems

from bluer_ugv.README.consts import algo_docs
from bluer_ugv.README.swallow.consts import swallow_assets2

docs = [
    {
        "path": "../docs/swallow/digital/algo/tracking",
    },
    {
        "path": "../docs/swallow/digital/algo/tracking/validations",
    },
    {
        "path": "../docs/swallow/digital/algo/tracking/validations/one.md",
        "items": ImageItems(
            {
                f"{swallow_assets2}/target-selection.png": f"{algo_docs}/socket.md",
            }
        ),
    },
]

from bluer_ai.env import BLUER_AI_SBC_PASSWORD

from bluer_ugv.README.swallow.digital import algo, design

docs = (
    [
        {
            "path": "../docs/swallow/digital",
        },
        {
            "path": "../docs/swallow/digital/manual.md",
            "macros": {
                "password:::": BLUER_AI_SBC_PASSWORD,
            },
        },
    ]
    + design.docs
    + algo.docs
)

from bluer_ugv.README.swallow.digital.design.arzhang4 import parts, tagline, v1

docs = (
    [
        {
            "path": "../docs/swallow/digital/design/arzhang4",
            "macros": {
                "tagline:::": tagline,
            },
        },
    ]
    + parts.docs
    + v1.docs
)

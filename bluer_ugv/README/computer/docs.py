from bluer_ugv.README.computer import box, pcb, power, schematics, testing


docs = (
    [
        {
            "path": "../docs/swallow/digital/design/computer",
        },
        {
            "path": "../docs/swallow/digital/design/computer/naming.md",
        },
        {
            "path": "../docs/swallow/digital/design/computer/connectors-v1.md",
        },
    ]
    + box.docs
    + pcb.docs
    + power.docs
    + schematics.docs
    + testing.docs
)

from bluer_ugv.README.shield import box, pcb, power, schematics, testing


docs = (
    [
        {
            "path": "../docs/swallow/digital/design/shield",
        },
        {
            "path": "../docs/swallow/digital/design/shield/connectors-v1.md",
        },
    ]
    + box.docs
    + pcb.docs
    + power.docs
    + schematics.docs
    + testing.docs
)

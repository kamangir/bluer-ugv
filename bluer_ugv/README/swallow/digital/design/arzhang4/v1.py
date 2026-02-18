from bluer_sbc.README.design import design_doc_parts

parts = {
    "DC-gearboxed-motor-12V-120RPM": "4 x, replacement gearboxes",
}

docs = [
    {
        "path": "../docs/swallow/digital/design/arzhang4/v1.md",
        "macros": design_doc_parts(
            dict_of_parts=parts,
            parts_reference="../parts",
        ),
    },
]

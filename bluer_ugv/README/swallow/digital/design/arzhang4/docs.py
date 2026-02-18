from bluer_sbc.README.design import design_doc_parts

from bluer_ugv.README.swallow.digital.design.arzhang4 import tagline, v1, parts

docs = [
    {
        "path": "../docs/swallow/digital/design/arzhang4",
        "macros": {
            **design_doc_parts(
                dict_of_parts=parts.dict_of_parts,
                parts_reference="repo",
            ),
            "tagline:::": tagline,
        },
    },
] + v1.docs

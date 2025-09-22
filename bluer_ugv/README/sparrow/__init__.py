from bluer_ugv.sparrow.README import items
from bluer_ugv.README.sparrow.algo import items as algo_items
from bluer_ugv.README.sparrow.design import items as design_items
from bluer_ugv.README.sparrow.validation import items as validation_items

docs = (
    [
        {
            "items": items,
            "path": "../docs/bluer_sparrow",
        }
    ]
    + design_items
    + algo_items
    + validation_items
)

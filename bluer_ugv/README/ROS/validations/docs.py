from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

from bluer_ugv.README.ROS.validations import arzhang4, basic, gazebo


docs = (
    [
        {
            "path": f"../docs/ROS/validations/{suffix}",
            "items": items,
        }
        for suffix, items in {
            "": [],
        }.items()
    ]
    + arzhang4.docs
    + basic.docs
    + gazebo.docs
)

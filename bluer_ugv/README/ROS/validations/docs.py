from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

from bluer_ugv.README.ROS.validations import gazebo


docs = [
    {
        "path": f"../docs/ROS/validations/{suffix}",
        "items": items,
    }
    for suffix, items in {
        "": [],
    }.items()
] + gazebo.docs

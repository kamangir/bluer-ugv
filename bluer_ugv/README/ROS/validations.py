from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

docs = [
    {
        "path": f"../docs/ROS/validations/{suffix}",
        "items": items,
    }
    for suffix, items in {
        "": [],
        "gazebo.md": ImageItems(
            {
                assets_url(
                    "ROS/gazebo.png",
                    volume=3,
                ): "",
            }
        ),
        "mac.md": [],
        "rpi.md": [],
    }.items()
]

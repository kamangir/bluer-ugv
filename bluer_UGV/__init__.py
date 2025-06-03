NAME = "bluer_UGV"

ICON = "🐬"

DESCRIPTION = f"{ICON} AI x ROS."

VERSION = "5.5.1"

REPO_NAME = "bluer-UGV"

MARQUEE = (
    "https://github.com/waveshareteam/ugv_rpi/raw/main/media/UGV-Rover-details-23.jpg"
)

ALIAS = "@UGV"


def fullname() -> str:
    return f"{NAME}-{VERSION}"

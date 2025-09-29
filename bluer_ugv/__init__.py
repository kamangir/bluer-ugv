from bluer_ugv.README.consts import assets2

NAME = "bluer_ugv"

ICON = "🐬"

DESCRIPTION = f"{ICON} AI x UGV."

VERSION = "6.955.1"

REPO_NAME = "bluer-ugv"

MARQUEE = f"{assets2}/bluer-sparrow/VID-20250905-WA0014_1.gif"


ALIAS = "@ugv"


def fullname() -> str:
    return f"{NAME}-{VERSION}"

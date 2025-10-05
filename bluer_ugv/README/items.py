from bluer_objects import README

from bluer_ugv.README.consts import (
    assets2_bluer_eagle,
    assets2_bluer_robin,
    assets2_arzhang,
    assets2_rangin,
    assets2_swallow,
    assets2_bluer_ugv,
)

items = README.Items(
    [
        {
            "name": "swallow",
            "marquee": f"{assets2_swallow}/20250913_203635~2_1.gif?raw=true",
            "description": "based on power wheels.",
            "url": "./bluer_ugv/docs/swallow",
        },
        {
            "name": "arzhang",
            "marquee": f"{assets2_arzhang}/VID-20250905-WA0014_1.gif?raw=true",
            "description": "[swallow](./bluer_ugv/docs/swallow)'s little sister.",
            "url": "./bluer_ugv/docs/arzhang",
        },
        {
            "name": "rangin",
            "marquee": f"{assets2_rangin}/rangin.png",
            "description": "[swallow](./bluer_ugv/docs/swallow)'s ad robot.",
            "url": "./bluer_ugv/docs/rangin.md",
        },
        {
            "name": "bluer-robin",
            "marquee": f"{assets2_bluer_robin}/20250723_095155~2_1.gif?raw=true",
            "description": "remote control car kit for teenagers.",
            "url": "./bluer_ugv/docs/bluer_robin",
        },
        {
            "name": "bluer-eagle",
            "marquee": f"{assets2_bluer_eagle}/file_0000000007986246b45343b0c06325dd.png?raw=true",
            "description": "a remotely controlled ballon.",
            "url": "./bluer_ugv/docs/bluer_eagle",
        },
        {
            "name": "bluer-fire",
            "marquee": f"{assets2_bluer_ugv}/bluer-fire.png?raw=true",
            "description": "based on a used car.",
            "url": "./bluer_ugv/docs/bluer_fire",
        },
        {
            "name": "bluer-beast",
            "marquee": "https://github.com/waveshareteam/ugv_rpi/raw/main/media/UGV-Rover-details-23.jpg",
            "description": "based on [UGV Beast PI ROS2](https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2).",
            "url": "./bluer_ugv/docs/bluer_beast",
        },
    ]
)

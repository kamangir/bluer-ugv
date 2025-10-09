from bluer_objects.README.items import ImageItems, Items
from bluer_objects.README.consts import assets, assets_url
from bluer_objects import markdown
from bluer_objects import env

from bluer_ugv.README.arzhang.consts import arzhang_assets2

dict_of_validations = {
    "village-1": {
        "ugv_name": "arzhang",
        "items": ImageItems(
            {
                f"{arzhang_assets2}/20250905_120526.jpg": "",
                f"{arzhang_assets2}/20250905_120808.jpg": "",
                f"{arzhang_assets2}/20250905_121030.jpg": "",
                f"{arzhang_assets2}/20250905_121032.jpg": "",
                f"{arzhang_assets2}/20250905_121702.jpg": "",
                f"{arzhang_assets2}/20250905_121711.jpg": "",
            }
        ),
        "marquee": f"{assets}/2025-09-05-11-48-27-d56azo/VID-20250905-WA0014_1.gif",
    },
    "village-2": {
        "ugv_name": "arzhang",
        "items": ImageItems(
            {
                f"{arzhang_assets2}/20250922_094548.jpg": "",
                f"{arzhang_assets2}/20250922_101156.jpg": "",
                f"{arzhang_assets2}/20250922_101409.jpg": "",
                f"{arzhang_assets2}/20250922_101557.jpg": "",
                f"{arzhang_assets2}/20250922_101653.jpg": "",
                f"{arzhang_assets2}/20250922_102822.jpg": "",
            }
        ),
        "macros": {
            "debug_objects": markdown.generate_table(
                Items(
                    [
                        {
                            "name": object_name,
                            "url": "https://{}.{}/{}".format(
                                env.S3_PUBLIC_STORAGE_BUCKET,
                                env.S3_STORAGE_ENDPOINT_URL.split("https://", 1)[1],
                                f"{object_name}.tar.gz",
                            ),
                            "marquee": f"{assets}/{object_name}/{object_name}.gif",
                        }
                        for object_name in [
                            "swallow-debug-2025-09-22-09-47-32-85hag3",
                            "swallow-debug-2025-09-22-09-59-29-emj29v",
                            "swallow-debug-2025-09-22-10-01-01-uzray6",
                            "swallow-debug-2025-09-22-10-06-19-hcyl1v",
                            "swallow-debug-2025-09-22-10-09-44-z6q9kn",
                            "swallow-debug-2025-09-22-10-19-35-mobajm",
                        ]
                    ]
                ),
                cols=3,
                log=False,
            ),
        },
        "marquee": f"{assets}/arzhang/20250922_101202_1.gif",
    },
    "village-3": {
        "ugv_name": "arzhang",
        "items": ImageItems(
            {
                f"{arzhang_assets2}/20250925_133136.jpg": "",
                f"{arzhang_assets2}/20250925_133628.jpg": "",
                f"{arzhang_assets2}/20250925_133637.jpg": "",
                f"{arzhang_assets2}/20250925_132521~2_1.gif": "",
            },
        ),
        "cols": 2,
        "marquee": assets_url(
            suffix="{object_name}/{object_name}.gif".format(
                object_name="swallow-debug-2025-09-25-13-16-59-rnm7jd"
            )
        ),
    },
    "village-4": {
        "ugv_name": "arzhang2",
        "items": ImageItems(
            {
                f"{arzhang_assets2}/20250927_192024.jpg": "",
            },
        ),
        "marquee": assets_url(
            suffix="{object_name}/{object_name}.gif".format(
                object_name="swallow-debug-2025-09-27-19-15-31-6iq5vz"
            )
        ),
    },
    "timing-review": {
        "ugv_name": "arzhang2",
        "marquee": assets_url(
            suffix="{object_name}/{object_name}.gif".format(
                object_name="swallow-debug-2025-10-09-17-04-47-vm23uf"
            )
        ),
    },
    "template": {
        "ugv_name": "template",
        "marquee": "template.jpg",
    },
}

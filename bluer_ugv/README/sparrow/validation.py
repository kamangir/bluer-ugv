from bluer_objects.README.items import ImageItems, Items
from bluer_objects import markdown
from bluer_objects import env

from bluer_ugv.README.consts import assets2, assets2_bluer_sparrow

items = [
    {
        "path": "../docs/bluer_sparrow/validation",
    },
    {
        "path": "../docs/bluer_sparrow/validation/village-1.md",
        "items": ImageItems(
            {
                f"{assets2_bluer_sparrow}/20250905_120526.jpg": "",
                f"{assets2_bluer_sparrow}/20250905_120808.jpg": "",
                f"{assets2_bluer_sparrow}/20250905_121030.jpg": "",
                f"{assets2_bluer_sparrow}/20250905_121032.jpg": "",
                f"{assets2_bluer_sparrow}/20250905_121702.jpg": "",
                f"{assets2_bluer_sparrow}/20250905_121711.jpg": "",
            }
        ),
    },
    {
        "path": "../docs/bluer_sparrow/validation/village-2.md",
        "items": ImageItems(
            {
                f"{assets2_bluer_sparrow}/20250922_094548.jpg": "",
                f"{assets2_bluer_sparrow}/20250922_101156.jpg": "",
                f"{assets2_bluer_sparrow}/20250922_101409.jpg": "",
                f"{assets2_bluer_sparrow}/20250922_101557.jpg": "",
                f"{assets2_bluer_sparrow}/20250922_101653.jpg": "",
                f"{assets2_bluer_sparrow}/20250922_102822.jpg": "",
            }
        ),
        "gifs": markdown.generate_table(
            Items(
                [
                    {"image": f"{assets2_bluer_sparrow}/20250922_101202_1.gif"},
                ]
                + [
                    {
                        "name": object_name,
                        "url": "🔗 https://{}.{}/{}".format(
                            env.S3_PUBLIC_STORAGE_BUCKET,
                            env.S3_STORAGE_ENDPOINT_URL.split("https://", 1)[1],
                            f"{object_name}.tar.gz",
                        ),
                        "marquee": f"{assets2}/{object_name}/{object_name}.gif",
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
        ),
    },
]

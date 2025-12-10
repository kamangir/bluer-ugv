from typing import List

from bluer_objects import storage
from bluer_objects.README.items import Items
from bluer_objects.README.consts import assets
from bluer_objects import markdown
from bluer_objects import env


def objects() -> List[str]:
    success, list_of_objects = storage.ls_objects(
        prefix="2025-12-09",
        where="cloud",
    )
    assert success

    return markdown.generate_table(
        Items(
            [
                {
                    "name": object_name,
                    "url": "https://{}.{}/{}".format(
                        env.S3_PUBLIC_STORAGE_BUCKET,
                        env.S3_STORAGE_ENDPOINT_URL.split("https://", 1)[1],
                        f"{object_name}.tar.gz",
                    ),
                    "marquee": f"{assets}/{object_name}/ultrasonic-sensor-pulse-ms.png",
                }
                for object_name in list_of_objects
            ]
        ),
        cols=len(list_of_objects),
        log=False,
    )

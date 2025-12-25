from typing import List

from bluer_objects import storage
from bluer_objects.README.items import Items
from bluer_objects.README.consts import assets
from bluer_objects import markdown
from bluer_objects import env


def objects(
    use_cache: bool = True,
) -> List[str]:
    if use_cache:
        list_of_objects = [
            "2025-12-09-08-16-53-a4rfg2",
            "2025-12-09-08-52-54-jre3xs",
            "2025-12-09-09-09-43-ljsjbb",
            "2025-12-09-10-51-24-2dfnau",
            "2025-12-09-14-36-28-3o4zvv",
            "2025-12-09-16-42-23-h1awiz",
            "2025-12-09-18-52-03-7jo931",
        ]
    else:
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
                    "marquee": f"{assets}/{object_name}/ultrasonic-sensor-state.png",
                }
                for object_name in list_of_objects
            ]
        ),
        cols=1,
        log=False,
    )

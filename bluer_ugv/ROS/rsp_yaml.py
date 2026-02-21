import sys
import os

from blueness import module
from bluer_objects import file

from bluer_ugv import NAME
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def generate_rsp_yaml(urdf_path: str) -> bool:
    yaml_path = os.path.join(
        file.path(urdf_path),
        "{}_rsp.yaml".format(
            file.name(
                urdf_path,
            )
        ),
    )

    logger.info(
        "{}.generate_rsp_yaml: {} -> {}".format(
            NAME,
            urdf_path,
            yaml_path,
        )
    )

    success, urdf = file.load_text(urdf_path)
    if not success:
        return success

    return file.save_text(
        yaml_path,
        [
            "robot_state_publisher:",
            "  ros__parameters:",
            "    robot_description: |",
        ]
        + [f"      {line}" for line in urdf]
        + [
            "",
        ],
    )

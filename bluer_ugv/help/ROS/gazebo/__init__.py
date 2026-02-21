from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_ugv.help.ROS.gazebo.gui import help_functions as help_gui


def help_publish_robot_description(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "gazebo",
            "publish_robot_description",
            f"[{options}]",
        ],
        "publish robot description.",
        mono=mono,
    )


help_functions = {
    "gui": help_gui,
    "publish_robot_description": help_publish_robot_description,
}

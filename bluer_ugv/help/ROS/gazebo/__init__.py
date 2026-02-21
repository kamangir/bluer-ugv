from typing import List

from bluer_options.terminal import show_usage

from bluer_ugv.help.ROS.gazebo.gui import help_functions as help_gui
from bluer_ugv.help.ROS.gazebo.robot import help_functions as help_robot


def help_log(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@ROS",
            "gazebo",
            "log",
        ],
        "log the state.",
        mono=mono,
    )


help_functions = {
    "log": help_log,
    "gui": help_gui,
    "robot": help_robot,
}

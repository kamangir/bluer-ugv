from typing import List

from bluer_options.terminal import show_usage, xtra


def help_control(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "angular=<0.0>",
            xtra(",dryrun,", mono=mono),
            "linear=<0.0>",
        ]
    )

    return show_usage(
        [
            "@ROS",
            "gazebo",
            "control",
            f"[{options}]",
        ],
        "control the robot.",
        {
            "angular": ["rotational velocity (rad/s)"],
            "linear": ["forward/backward velocity (m/s)"],
        },
        mono=mono,
    )


def help_publish(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "gazebo",
            "robot",
            "publish",
            f"[{options}]",
        ],
        "publish robot description.",
        mono=mono,
    )


def help_spawn(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "gazebo",
            "robot",
            "spawn",
            f"[{options}]",
        ],
        "spawn robot.",
        mono=mono,
    )


help_functions = {
    "control": help_control,
    "publish": help_publish,
    "spawn": help_spawn,
}

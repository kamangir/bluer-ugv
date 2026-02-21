from typing import List

from bluer_options.terminal import show_usage, xtra


def help_open(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "gazebo",
            "gui",
            "open",
            f"[{options}]",
        ],
        "open gazebo gui.",
        mono=mono,
    )


def help_serve(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "gazebo",
            "gui",
            "serve",
            f"[{options}]",
        ],
        "serve gazebo gui.",
        mono=mono,
    )


help_functions = {
    "open": help_open,
    "serve": help_serve,
}

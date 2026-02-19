from typing import List

from bluer_options.terminal import show_usage, xtra


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@ROS",
            "install",
        ],
        "install ROS.",
        mono=mono,
    )


help_functions = {
    "install": help_install,
}

from typing import List

from bluer_options.terminal import show_usage, xtra


def help_build(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "package",
            "build",
            "<package-name>",
            f"[{options}]",
        ],
        "build package.",
        mono=mono,
    )


def help_create(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "package",
            "create",
            "<package-name>",
            f"[{options}]",
        ],
        "create package.",
        mono=mono,
    )


help_functions = {
    "build": help_build,
    "create": help_create,
}

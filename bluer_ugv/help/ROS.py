from typing import List

from bluer_options.terminal import show_usage, xtra


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "install",
            f"[{options}]",
        ],
        "install ROS.",
        mono=mono,
    )


def help_open(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "open",
            f"[{options}]",
        ],
        "open ROS.",
        mono=mono,
    )


def help_start(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~build,~cache,dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "start",
            f"[{options}]",
        ],
        "start ROS.",
        mono=mono,
    )


def help_stop(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@ROS",
            "stop",
            f"[{options}]",
        ],
        "stop ROS.",
        mono=mono,
    )


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "talker|listener",
        ]
    )

    return show_usage(
        [
            "@ROS",
            "test",
            f"[{options}]",
        ],
        "test ROS.",
        mono=mono,
    )


help_functions = {
    "install": help_install,
    "open": help_open,
    "start": help_start,
    "stop": help_stop,
    "test": help_test,
}

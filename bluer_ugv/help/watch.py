from typing import List

from bluer_options.terminal import show_usage


def help_watch(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@ugv",
            "watch",
            "<ugv-name>",
            "back | front | top",
        ],
        "watch <ugv-name>.",
        mono=mono,
    )

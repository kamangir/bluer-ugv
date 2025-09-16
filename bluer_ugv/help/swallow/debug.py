from typing import List

from bluer_options.terminal import show_usage


def help_debug(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--host <hostname>]",
        "[--loop 0]",
    ]

    return show_usage(
        [
            "@swallow",
            "debug",
        ]
        + args,
        "debug swallow.",
        mono=mono,
    )

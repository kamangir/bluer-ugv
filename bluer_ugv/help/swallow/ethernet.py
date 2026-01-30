from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_ugv import env


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@swallow",
            "ethernet",
            "test",
            f"[{options}]",
        ],
        "test ethernet.",
        mono=mono,
    )


help_functions = {
    "test": help_test,
}

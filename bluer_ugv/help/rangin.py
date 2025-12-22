from typing import List

from bluer_options.terminal import show_usage, xtra


def help_init(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("install", mono=mono)

    return show_usage(
        [
            "@rangin",
            "init",
            f"[{options}]",
        ],
        "init.",
        mono=mono,
    )


help_functions = {
    "init": help_init,
}

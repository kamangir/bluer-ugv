from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_plugin import ALIAS
from bluer_plugin.help.node.functions import help_functions as help_node


def help_adjust(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dryrun"

    args = [
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@ugv",
            "parts",
            "adjust",
            f"[{options}]",
        ]
        + args,
        "adjust part images.",
        mono=mono,
    )


help_functions = {
    "adjust": help_adjust,
}

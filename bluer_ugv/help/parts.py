from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_plugin import ALIAS
from bluer_plugin.help.node.functions import help_functions as help_node


def help_adjust_images(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dryrun"

    return show_usage(
        [
            "@ugv",
            "parts",
            "adjust_images",
            f"[{options}]",
        ],
        "adjust part images.",
        mono=mono,
    )


help_functions = {
    "adjust_images": help_adjust_images,
}

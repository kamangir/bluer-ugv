from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_plugin import ALIAS
from bluer_plugin.help.node.functions import help_functions as help_node


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        "[--host <host-name>]",
        "[--what receiving | sending]",
    ]

    return show_usage(
        [
            "@ugv",
            "socket",
            "test",
            f"[{options}]",
        ]
        + args,
        "test socket.",
        mono=mono,
    )


help_functions = {
    "test": help_test,
}

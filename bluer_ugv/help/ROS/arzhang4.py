from typing import List

from bluer_options.terminal import show_usage, xtra


def help_run(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~build,dryrun", mono=mono)

    return show_usage(
        [
            "@arzhang4",
            "run",
            f"[{options}]",
            "<node-name>]",
        ],
        "run <node-name>.",
        {
            "node-name: motor_driver | teleop": "",
        },
        mono=mono,
    )


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~build,dryrun", mono=mono)

    return show_usage(
        [
            "@arzhang4",
            "test",
            f"[{options}]",
            "<node-name>",
        ],
        "test <node-name>.",
        {
            "node-name: teleop": "",
        },
        mono=mono,
    )


help_functions = {
    "run": help_run,
    "test": help_test,
}

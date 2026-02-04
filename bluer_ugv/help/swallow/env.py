from typing import List, Dict

from bluer_options.terminal import show_usage
from bluer_sbc import env

dict_of_variables: Dict[str, Dict] = {
    "bps": {
        "name": "BLUER_SBC_SWALLOW_HAS_BPS",
        "value": env.BLUER_SBC_SWALLOW_HAS_BPS,
    },
    "camera": {
        "name": "BLUER_SBC_SWALLOW_HAS_CAMERA",
        "value": env.BLUER_SBC_SWALLOW_HAS_CAMERA,
    },
    "dev_mode": {
        "name": "BLUER_SBC_SWALLOW_DEV_MODE",
        "value": env.BLUER_SBC_SWALLOW_DEV_MODE,
    },
    "full_keyboard": {
        "name": "BLUER_SBC_SWALLOW_HAS_FULL_KEYBOARD",
        "value": env.BLUER_SBC_SWALLOW_HAS_FULL_KEYBOARD,
    },
    "screen": {
        "name": "BLUER_SBC_ENABLE_SCREEN",
        "value": env.BLUER_SBC_ENABLE_SCREEN,
    },
    "steering": {
        "name": "BLUER_SBC_SWALLOW_HAS_STEERING",
        "value": env.BLUER_SBC_SWALLOW_HAS_STEERING,
    },
}


def help_cat(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@swallow",
            "env",
            "cat",
            "[<env-name>]",
        ],
        "cat swallow-raspbian-<env-name>.env.",
        mono=mono,
    )


def help_cd(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@swallow",
            "env",
            "cd",
        ],
        "cd env folder.",
        mono=mono,
    )


def help_cp(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@swallow",
            "env",
            "cp",
            "[<env-name>]",
        ],
        "cp swallow-raspbian-<env-name>.env.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@swallow",
            "env",
            "list",
        ],
        "list swallow envs.",
        mono=mono,
    )


def help_set(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@swallow",
            "env",
            "set",
            " | ".join(sorted(dict_of_variables.keys())),
            "0 | 1",
        ],
        "set env.",
        {
            "{}: {} (currently: {})".format(
                keyword,
                info["name"],
                info["value"],
            ): ""
            for keyword, info in dict_of_variables.items()
        },
        mono=mono,
    )


help_functions = {
    "cat": help_cat,
    "cd": help_cd,
    "cp": help_cp,
    "list": help_list,
    "set": help_set,
}

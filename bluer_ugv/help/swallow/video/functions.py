from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_ugv import env
from bluer_ugv.help.swallow.video.playlist import help_functions as help_playlist


def help_pause(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@swallow",
            "video",
            "pause",
            f"[{options}]",
        ],
        "pause video player.",
        mono=mono,
    )


def help_play(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "download",
            xtra(",dryrun,", mono=mono),
            "video=<loading|1>",
        ]
    )

    "download,dryrun,video=<loading|1>"

    return show_usage(
        [
            "@swallow",
            "video",
            "play",
            f"[{options}]",
            "[{}|<object-name>]".format(env.RANGIN_VIDEO_LIST_OBJECT),
        ],
        "play <object-name>.",
        mono=mono,
    )


def help_stop(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@swallow",
            "video",
            "stop",
            f"[{options}]",
        ],
        "stop video player.",
        mono=mono,
    )


help_functions = {
    "pause": help_pause,
    "play": help_play,
    "playlist": help_playlist,
    "stop": help_stop,
}

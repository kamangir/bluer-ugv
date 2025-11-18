from typing import List

from bluer_options.terminal import show_usage

from bluer_ugv import env
from bluer_ugv.help.swallow.video.playlist import help_functions as help_playlist


def help_pause(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@swallow",
            "video_player",
            "pause",
        ],
        "pause video player.",
        mono=mono,
    )


def help_play(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "download,video=<loading|1>"

    return show_usage(
        [
            "@swallow",
            "video_player",
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
    return show_usage(
        [
            "@swallow",
            "video_player",
            "stop",
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

import pytest

from bluer_ugv.swallow.session.classical.screen.video.playlist import PlayList
from bluer_ugv.swallow.session.classical.screen.video.player import (
    VideoPlayer,
    VideoEngine,
)
from bluer_ugv import env


@pytest.mark.parametrize(
    [
        "engine",
    ],
    [[engine] for engine in VideoEngine],
)
@pytest.mark.parametrize(
    [
        "fullscreen",
    ],
    [[True], [False]],
)
@pytest.mark.parametrize(
    [
        "loop",
    ],
    [[True], [False]],
)
@pytest.mark.parametrize(
    [
        "audio",
    ],
    [[True], [False]],
)
def test_screen_video_player_engine(
    engine: VideoEngine,
    fullscreen: bool,
    loop: bool,
    audio: bool,
):
    assert isinstance(
        engine.play_command(
            filename="filename.mp4",
            fullscreen=fullscreen,
            loop=loop,
            audio=audio,
        ),
        str,
    )


def test_screen_video_player():
    playlist = PlayList(env.RANGIN_VIDEO_LIST_OBJECT)

    video_player = VideoPlayer(dryrun=True)

    assert video_player.play(playlist.get())

    assert video_player.pause()

    assert video_player.stop()

    assert video_player.play(playlist.get("loading"))

    assert video_player.play(playlist.get(1))

    assert video_player.play(playlist.get("1"))

    assert video_player.stop()

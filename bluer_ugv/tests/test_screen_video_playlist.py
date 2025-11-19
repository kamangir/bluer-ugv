import pytest

from bluer_objects import file

from bluer_ugv.swallow.session.classical.screen.video.playlist import PlayList
from bluer_ugv import env


def test_screen_video_playlist():
    playlist = PlayList(env.RANGIN_VIDEO_LIST_OBJECT)
    assert playlist.messages
    assert playlist.playlist

    playlist.next()
    assert playlist.index == 0
    playlist.next()
    assert playlist.index == 1
    playlist.next()
    assert playlist.index == 0


@pytest.mark.parametrize(
    ["keyword", "expected_to_exist"],
    [
        ["loading", True],
        ["warning", True],
        ["void", False],
        [0, True],
        [1, True],
        ["1", True],
        [999, False],
    ],
)
@pytest.mark.parametrize(
    [
        "what",
    ],
    [
        ["filename"],
        ["source"],
        ["void"],
    ],
)
def test_screen_video_playlist_get(
    keyword: str | int,
    expected_to_exist: bool,
    what: str,
):
    playlist = PlayList(env.RANGIN_VIDEO_LIST_OBJECT)

    assert isinstance(playlist.get(keyword), str), keyword

    thing = playlist.get(keyword, what=what)

    assert isinstance(thing, str), f"{keyword}.{what}"

    if what == "filename" and expected_to_exist:
        assert file.exists(filename=thing)

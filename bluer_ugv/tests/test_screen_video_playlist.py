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

    for keyword in [
        "loading",
        "warning",
        "void",
        0,
        1,
        999,
    ]:
        assert isinstance(
            playlist.get(keyword),
            str,
        ), keyword

        for what in ["filename", "source"]:
            thing = playlist.get(
                keyword,
                what=what,
            )

            assert isinstance(thing, str), f"{keyword}.{what}"

            if what == "filename":
                assert file.exists(filename=what)

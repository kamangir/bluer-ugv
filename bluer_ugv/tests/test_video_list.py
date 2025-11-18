from bluer_ugv.swallow.session.classical.screen.video_list import VideoList
from bluer_ugv import env


def test_video_list():
    video_list = VideoList(env.RANGIN_VIDEO_LIST_OBJECT)
    assert video_list.messages
    assert video_list.play_list

    video_list.next()
    assert video_list.index == 0
    video_list.next()
    assert video_list.index == 1
    video_list.next()
    assert video_list.index == 0

    for keyword in [
        "loading",
        "warning",
        "void",
        0,
        1,
        999,
    ]:
        assert isinstance(
            video_list.get(keyword),
            str,
        ), keyword

        for what in ["filename", "source"]:
            assert isinstance(
                video_list.get(
                    keyword,
                    what=what,
                ),
                str,
            ), f"{keyword}.{what}"

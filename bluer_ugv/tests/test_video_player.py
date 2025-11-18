from bluer_ugv.swallow.session.classical.screen.video_list import VideoList
from bluer_ugv.swallow.session.classical.screen.video_player import VideoPlayer
from bluer_ugv import env


def test_video_player():
    video_list = VideoList(env.RANGIN_VIDEO_LIST_OBJECT)

    video_player = VideoPlayer(dryrun=True)

    assert video_player.play(video_list.get(0))

    assert video_player.pause()

    assert video_player.stop()

    assert video_player.play(video_list.get(1))

    assert video_player.stop()

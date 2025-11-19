from bluer_ugv.swallow.session.classical.screen.video.playlist import PlayList
from bluer_ugv.swallow.session.classical.screen.video.player import VideoPlayer
from bluer_ugv import env


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

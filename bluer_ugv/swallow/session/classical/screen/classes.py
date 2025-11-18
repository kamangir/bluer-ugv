from bluer_options.host.functions import is_headless

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.screen.video_player import VideoPlayer
from bluer_ugv.swallow.session.classical.screen.video_list import VideoList
from bluer_ugv.logger import logger


class ClassicalScreen:
    def __init__(self):
        self.video_player = None if is_headless() else VideoPlayer()

        self.video_list = VideoList(env.RANGIN_VIDEO_LIST_OBJECT)

        logger.info(f"{self.__class__.__name__} created.")

    def cleanup(self):
        self.video_player.stop()

    def initialize(self) -> bool:
        return self.video_player.play(
            self.video_list.get("loading"),
            loop=True,
        )

    def update(self) -> bool:
        if self.video_player.process:
            return True

        self.video_list.next()

        return self.video_player.play(
            self.video_list.get(self.video_list.index),
            loop=False,
        )

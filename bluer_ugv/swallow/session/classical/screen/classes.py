from bluer_options.host.functions import is_headless

from bluer_ugv.logger import logger
from bluer_ugv import env
from bluer_ugv.swallow.session.classical.screen.video_player import VideoPlayer
from bluer_ugv.swallow.session.classical.screen.video_list import VideoList


class ClassicalScreen:
    def __init__(self):
        self.video_player = None if is_headless() else VideoPlayer()

        self.video_list = VideoList(env.RANGIN_VIDEO_LIST_OBJECT)
        self.video_list_index = -1

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

        self.video_list_index += 1
        if self.video_list_index >= len(self.video_list.play_list):
            self.video_list_index = 0

        logger.info(
            "{}: video #{}".format(
                self.__class__.__name__,
                self.video_list_index,
            )
        )

        return self.video_player.play(
            self.video_list.get(self.video_list_index),
            loop=False,
        )

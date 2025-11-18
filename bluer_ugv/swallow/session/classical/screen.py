from typing import List

from bluer_options.host.functions import is_headless
from bluer_options.logger.config import log_list

from bluer_ugv.logger import logger


class ClassicalScreen:
    def __init__(self):
        if is_headless():
            return

        logger.info(f"{self.__class__.__name__} created.")

    def cleanup(self):
        logger.info("🪄")

        logger.info(f"{self.__class__.__name__}.cleanup")

    def stop(self):
        # stop playing.

        logger.info(f"{self.__class__.__name__}.stop")

    def pause(self, filename: str):
        # pause playing.

        logger.info(f"{self.__class__.__name__}.play({filename})")

    def play(self, filename: str):
        # play filename in a loop.

        logger.info(f"{self.__class__.__name__}.play({filename})")

    def play_list(self, playlist: List[str]):
        # play playlist in a loop

        log_list(
            logger,
            "play list",
            playlist,
            "filename(s)",
        )

    @staticmethod
    def length_of(filename: str) -> int:
        # return length of video in seconds.
        return 0

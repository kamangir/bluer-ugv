import threading
import time


from bluer_sbc.env import BLUER_SBC_AUDIO_ENABLED

from bluer_ugv.logger import logger


class ClassicalAudio:
    def __init__(
        self,
    ):
        self.enabled = BLUER_SBC_AUDIO_ENABLED == 1
        logger.info(
            "{}: {}".format(
                self.__class__.__name__,
                ("enabled" if self.enabled else "disabled"),
            )
        )

        self.running = False

        if not self.enabled:
            return

        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def stop(self):
        if not self.enabled:
            return

        self.running = False
        self.thread.join()

        logger.info(f"{self.__class__.__name__}.stopped.")

    def loop(self):
        logger.info(f"{self.__class__.__name__}.loop started.")

        while self.running:
            time.sleep(5)
            logger.info("audio loop 🪄")

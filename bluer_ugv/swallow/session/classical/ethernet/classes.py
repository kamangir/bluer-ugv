import threading
import time


from bluer_ugv.swallow.session.classical.keyboard.classes import ClassicalKeyboard
from bluer_ugv.logger import logger


class ClassicalEthernet:
    def __init__(
        self,
        keyboard: ClassicalKeyboard,
    ):
        logger.info(f"{self.__class__.__name__} created.")

        self.keyboard = keyboard

        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

        logger.info(f"{self.__class__.__name__}.stopped.")

        # TODO

    def loop(self):
        logger.info(f"{self.__class__.__name__}.loop started.")

        while self.running:
            # TODO

            time.sleep(0.1)

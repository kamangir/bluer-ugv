from RPi import GPIO  # type: ignore

from bluer_ugv.logger import logger


class ClassicalButton:
    def __init__(self):
        self.pin = 26
        self.state = False

        self.press_time: int = 0
        self.press_duration: int = -1

    def initialize(self) -> bool:
        try:
            GPIO.setup(
                self.pin,
                GPIO.IN,
                pull_up_down=GPIO.PUD_UP,
            )
        except Exception as e:
            logger.error(e)
            return False

        return True

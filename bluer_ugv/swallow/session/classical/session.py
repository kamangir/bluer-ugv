import time
from RPi import GPIO  # type: ignore

from bluer_ugv.swallow.session.classical.push_button import ClassicalPushButton
from bluer_ugv.swallow.session.classical.keyboard import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.mousepad import ClassicalMousePad
from bluer_ugv.logger import logger


class ClassicalSession:
    def __init__(self):
        self.leds = ClassicalLeds()

        self.mousepad = ClassicalMousePad(self.leds)
        self.keyboard = ClassicalKeyboard(self.mousepad)
        self.push_button = ClassicalPushButton(self.leds)

        logger.info(f"{self.__class__.__name__}: created...")

    def initialize(self) -> bool:
        try:
            GPIO.setmode(GPIO.BCM)
        except Exception as e:
            logger.error(e)
            return False

        if not self.push_button.initialize():
            return False

        if not self.leds.initialize():
            return False

        return True

    def update(self) -> bool:
        return all(
            [
                self.keyboard.update(),
                self.push_button.update(),
                self.leds.update(),
            ]
        )

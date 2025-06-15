import time
from RPi import GPIO  # type: ignore

from bluer_sbc.session.functions import reply_to_bash

from bluer_ugv.swallow.session.classical.button import ClassicalButton
from bluer_ugv.swallow.session.classical.keyboard import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.led import ClassicalLeds
from bluer_ugv.swallow.session.classical.mousepad import ClassicalMousePad
from bluer_ugv.logger import logger


class ClassicalSession:
    def __init__(self):
        self.leds = ClassicalLeds()

        self.button = ClassicalButton(self.leds)
        self.keyboard = ClassicalKeyboard()
        self.mousepad = ClassicalMousePad(self.leds)

        logger.info("{} created...".format(self.__class__.__name__))

    def initialize(self) -> bool:
        try:
            GPIO.setmode(GPIO.BCM)
        except Exception as e:
            logger.error(e)
            return False

        if not self.button.initialize():
            return False

        if not self.leds.initialize():
            return False

        return True

    def update(self) -> bool:
        return all(
            [
                self.button.update(),
                self.keyboard.update(),
                self.leds.update(),
            ]
        )

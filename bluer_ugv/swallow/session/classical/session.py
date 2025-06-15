import keyboard
import time
from RPi import GPIO  # type: ignore

from bluer_options import string
from bluer_sbc.session.functions import reply_to_bash

from bluer_ugv.swallow.session.classical.button import ClassicalButton
from bluer_ugv.swallow.session.classical.led import ClassicalLeds
from bluer_ugv.swallow.session.classical.mousepad import ClassicalMousePad
from bluer_ugv.logger import logger

bash_keys = {
    "e": "exit",
    "r": "reboot",
    "s": "shutdown",
    "u": "update",
}

BUTTON_PRESS_DURATION_UPDATE = 5
BUTTON_PRESS_DURATION_SHUTDOWN = 10
BUTTON_PRESS_DURATION_IGNORE = 15


class ClassicalSession:
    def __init__(self):
        self.button = ClassicalButton()
        self.leds = ClassicalLeds()
        self.mousepad = ClassicalMousePad()

        logger.info(
            "{} created: {}".format(
                self.__class__.__name__,
                ", ".join(
                    [f"{key}:{action}" for key, action in bash_keys.items()],
                ),
            )
        )

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

    def button_command(self) -> bool:
        button_pressed = not GPIO.input(self.button.pin)
        if button_pressed:
            if not self.button.state:
                logger.info("button pressed.")
                self.button.press_time = time.time()

            self.button.press_duration = time.time() - self.button.press_time
            if self.button.press_duration > BUTTON_PRESS_DURATION_IGNORE:
                self.leds.leds["red"]["state"] = False
            elif self.button.press_duration > BUTTON_PRESS_DURATION_SHUTDOWN:
                self.leds.leds["red"]["state"] = True
            elif self.button.press_duration > BUTTON_PRESS_DURATION_UPDATE:
                self.leds.leds["red"]["state"] = not self.leds.leds["red"]["state"]
        else:
            if self.button.state:
                logger.info(
                    "button released after {}.".format(
                        string.pretty_duration(
                            self.button.press_duration,
                        )
                    )
                )

            if self.button.press_duration < BUTTON_PRESS_DURATION_IGNORE:
                if self.button.press_duration > BUTTON_PRESS_DURATION_SHUTDOWN:
                    reply_to_bash("shutdown")
                    return True

                if self.button.press_duration > BUTTON_PRESS_DURATION_UPDATE:
                    reply_to_bash("update")
                    return True

        self.button.state = button_pressed

        self.leds.leds["yellow"]["state"] = self.button.state

        return False

    def key_command(self) -> bool:
        for key, event in bash_keys.items():
            if keyboard.is_pressed(key):
                reply_to_bash(event)
                return True

        return False

import keyboard

from bluer_sbc.session.functions import reply_to_bash

from bluer_ugv.swallow.session.classical.setpoint import ClassicalSetPoint
from bluer_ugv.logger import logger

bash_keys = {
    "e": "exit",
    "r": "reboot",
    "s": "shutdown",
    "u": "update",
}


class ClassicalKeyboard:
    def __init__(
        self,
        setpoint: ClassicalSetPoint,
    ):
        logger.info(
            "{}: {}".format(
                self.__class__.__name__,
                ", ".join(
                    [f"{key}:{action}" for key, action in bash_keys.items()],
                ),
            )
        )

        self.setpoint = setpoint

    def update(self) -> bool:
        for key, event in bash_keys.items():
            if keyboard.is_pressed(key):
                reply_to_bash(event)
                return False

        if keyboard.is_pressed(" "):
            self.setpoint.stop()

        if keyboard.is_pressed("x"):
            self.setpoint.start()

        return True

import keyboard

from bluer_sbc.session.functions import reply_to_bash

from bluer_ugv.logger import logger

bash_keys = {
    "e": "exit",
    "r": "reboot",
    "s": "shutdown",
    "u": "update",
}


class ClassicalKeyboard:
    def __init__(self):
        logger.info(
            "{}: {}".format(
                self.__class__.__name__,
                ", ".join(
                    [f"{key}:{action}" for key, action in bash_keys.items()],
                ),
            )
        )

    def update(self) -> bool:
        for key, event in bash_keys.items():
            if keyboard.is_pressed(key):
                reply_to_bash(event)
                return False

        return True

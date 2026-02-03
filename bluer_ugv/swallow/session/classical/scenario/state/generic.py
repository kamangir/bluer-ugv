import copy
from typing import Dict, Union, Tuple

from bluer_ugv.swallow.session.classical.keyboard.classes import ClassicalKeyboard
from bluer_ugv.logger import logger


class GenericState:
    name = "generic"

    def __init__(
        self,
        keyboard: ClassicalKeyboard,
    ):
        self.keyboard = keyboard

        logger.info(f"created {self.__class__.__name__}")

    def close(self) -> bool:
        logger.info(f"closing {self.name} ...")
        return True

    def decide_state_change(self) -> Tuple[bool, str]:
        return False, ""

    def open(self) -> bool:
        logger.info(f"opening {self.name} ...")
        return True

    def process(self) -> bool:
        return True

import copy
from typing import Tuple

from bluer_ugv.swallow.session.classical.camera.generic import ClassicalCamera
from bluer_ugv.swallow.session.classical.keyboard.classes import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv.swallow.session.classical.scenario.state.logger import logger


class GenericState:
    name = "generic"

    def __init__(
        self,
        keyboard: ClassicalKeyboard,
        camera: ClassicalCamera,
        setpoint: ClassicalSetPoint,
    ):
        self.keyboard = keyboard
        self.camera = camera
        self.setpoint = setpoint

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

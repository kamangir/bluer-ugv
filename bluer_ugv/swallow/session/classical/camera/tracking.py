from typing import Tuple

from bluer_sbc.imager.camera import instance as camera
from bluer_algo.tracker.classes.target import Target

from bluer_ugv.swallow.session.classical.camera.generic import ClassicalCamera
from bluer_ugv.swallow.session.classical.camera.generic import ClassicalCamera
from bluer_ugv.swallow.session.classical.keyboard import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.setpoint import ClassicalSetPoint
from bluer_ugv.logger import logger


class ClassicalTrackingCamera(ClassicalCamera):
    def __init__(
        self,
        keyboard: ClassicalKeyboard,
        leds: ClassicalLeds,
        setpoint: ClassicalSetPoint,
        object_name: str,
    ):
        super().__init__(keyboard, leds, setpoint, object_name)

        self.track_window: Tuple[int, int, int, int] = None

    def initialize(self) -> bool:
        if not super().initialize():
            return False

        success, image = camera.capture(
            close_after=False,
            open_before=False,
            log=True,
        )
        if not success:
            return success

        self.leds.set_all(True)
        success, self.track_window = Target.select(
            image,
            local=False,
        )
        self.leds.set_all(False)
        if not success:
            return success

        logger.info(f"track_window: {self.track_window}")

        return True

from typing import Dict, Union, Tuple

from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState
from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.logger import logger


class ApproachingState(GenericState):
    name: str = "approaching"
    area_threshold = 0.2

    def close(self) -> bool:
        return super().close()

    def decide_state_change(self) -> Tuple[bool, str]:
        if self.camera.detection.area >= self.area_threshold:
            logger.info(
                "detection.area={:.2f} >= {:.2f}!".format(
                    self.camera.detection.area,
                    self.area_threshold,
                )
            )
            return True, "greeting"

        return super().decide_state_change()

    def open(self) -> bool:
        logger.info("setting keyboard mode to action.")
        self.keyboard.set("mode", OperationMode.ACTION)
        return super().open()

    def process(self) -> bool:
        return super().process()

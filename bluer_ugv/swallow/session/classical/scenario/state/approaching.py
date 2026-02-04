from typing import Tuple
import time

from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState
from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.swallow.session.classical.scenario.state.logger import logger


class ApproachingState(GenericState):
    name: str = "approaching"
    area_threshold = 0.2

    def close(self) -> bool:
        super().close()

        self.config.set("mode", OperationMode.NONE)
        time.sleep(1)

        self.setpoint.stop()

        return True

    def decide_state_change(self) -> Tuple[bool, str]:
        if self.camera.detection.area >= self.area_threshold:
            logger.info(
                "detection.area={:.2f} >= {:.2f}!".format(
                    self.camera.detection.area,
                    self.area_threshold,
                )
            )
            return True, "speaking"

        return super().decide_state_change()

    def open(self) -> bool:
        super().open()

        self.config.set("mode", OperationMode.ACTION)

        return True

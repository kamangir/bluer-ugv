import threading

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.scenario.state.machines.factory import (
    dict_of_state_machines,
    GenericStateMachine,
)
from bluer_ugv.logger import logger


class ClassicalScenario:
    def __init__(
        self,
    ):
        logger.info(self.__class__.__name__)

        self._lock = threading.Lock()

        with self._lock:
            self.state_machine = dict_of_state_machines.get(
                env.BLUER_UGV_SWALLOW_SCENARIO,
                GenericStateMachine,
            )()

    def update(self) -> bool:
        with self._lock:
            return self.state_machine.process()

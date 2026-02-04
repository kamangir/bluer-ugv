import threading

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.scenario.state.machines.factory import (
    dict_of_state_machines,
    GenericStateMachine,
)
from bluer_ugv.swallow.session.classical.config import ClassicalConfig
from bluer_ugv.swallow.session.classical.camera.generic import ClassicalCamera
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv.logger import logger


class ClassicalScenario:
    def __init__(
        self,
        config: ClassicalConfig,
        camera: ClassicalCamera,
        setpoint: ClassicalSetPoint,
    ):
        self.config = config
        self.camera = camera
        self.setpoint = setpoint

        logger.info(f"created {self.__class__.__name__}")

        self._lock = threading.Lock()

        with self._lock:
            self.state_machine = dict_of_state_machines.get(
                env.BLUER_UGV_SWALLOW_SCENARIO,
                GenericStateMachine,
            )(
                config=self.config,
                camera=self.camera,
                setpoint=self.setpoint,
            )

    def update(self) -> bool:
        with self._lock:
            return self.state_machine.process()

    def stop(self):
        with self._lock:
            self.state_machine.stop()

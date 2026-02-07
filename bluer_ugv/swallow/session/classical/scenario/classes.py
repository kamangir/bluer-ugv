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
        self.running = False

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

        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def loop(self) -> bool:
        logger.info(f"{self.__class__.__name__}.loop started.")

        while self.running:
            with self._lock:
                return self.state_machine.process()

    def stop(self):
        self.running = False
        self.thread.join()

        logger.info(f"{self.__class__.__name__}.stopped.")

        with self._lock:
            self.state_machine.stop()

from bluer_algo.socket.connection import DEV_HOST

from bluer_ugv.swallow.session.classical.config.classes import ClassicalConfig
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv.logger import logger


class ClassicalController:
    def __init__(
        self,
        config: ClassicalConfig,
        leds: ClassicalLeds,
        setpoint: ClassicalSetPoint,
    ):
        self.config = config
        self.leds = leds
        self.setpoint = setpoint

        self.special_key: bool = False

        logger.info(f"created {self.__class__.__name__}")

    def set_debug(self, value: bool):
        self.special_key = False

        self.config.set("debug_mode", value)

        logger.info(
            f'debug enabled, run "@swallow debug" on {DEV_HOST}.'
            if value
            else logger.info("debug disabled")
        )

    def set_special_key(self):
        self.special_key = True

        logger.info("🛠️ special key enabled.")

    def set_ultrasonic(self, value):
        self.special_key = False

        self.config.set("ultrasound_enabled", value)

    def update(self) -> bool:
        if self.special_key:
            self.leds.flash_all()

        return True

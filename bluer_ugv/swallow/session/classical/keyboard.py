import keyboard

from bluer_sbc.session.functions import reply_to_bash
from bluer_algo.socket.classes import DEV_HOST

from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv import env
from bluer_ugv.logger import logger

bash_keys = {
    "i": "exit",
    "o": "shutdown",
    "p": "reboot",
    "u": "update",
}


class ClassicalKeyboard:
    def __init__(
        self,
        leds: ClassicalLeds,
        setpoint: ClassicalSetPoint,
    ):
        logger.info(
            "{}: {}".format(
                self.__class__.__name__,
                ", ".join(
                    [f"{key}:{action}" for key, action in bash_keys.items()],
                ),
            )
        )

        self.leds = leds

        self.last_key: str = ""
        self.setpoint = setpoint

        self.mode = OperationMode.NONE

        self.debug_mode: bool = False

        self.special_key: bool = False

    def update(self) -> bool:
        self.last_key = ""

        mode = self.mode

        if self.special_key:
            for key, event in bash_keys.items():
                if keyboard.is_pressed(key):
                    reply_to_bash(event)
                    return False

        if keyboard.is_pressed(" "):
            self.special_key = False
            self.setpoint.stop()

        if keyboard.is_pressed("x"):
            self.special_key = False
            self.setpoint.start()

        if keyboard.is_pressed("a"):
            self.special_key = False
            self.last_key = "a"
            self.setpoint.put(
                what="steering",
                value=env.BLUER_UGV_SWALLOW_STEERING_SETPOINT,
            )
        elif keyboard.is_pressed("d"):
            self.special_key = False
            self.last_key = "d"
            self.setpoint.put(
                what="steering",
                value=-env.BLUER_UGV_SWALLOW_STEERING_SETPOINT,
            )
        else:
            self.setpoint.put(
                what="steering",
                value=0,
                log=False,
            )

        if keyboard.is_pressed("s"):
            self.special_key = False
            self.setpoint.put(
                what="speed",
                value=self.setpoint.get(what="speed") - 10,
            )

        if keyboard.is_pressed("w"):
            self.special_key = False
            self.setpoint.put(
                what="speed",
                value=self.setpoint.get(what="speed") + 10,
            )

        if keyboard.is_pressed("y"):
            self.special_key = False
            self.mode = OperationMode.NONE

        if keyboard.is_pressed("b"):
            if self.special_key:
                self.debug_mode = False
            else:
                self.debug_mode = True

            self.special_key = False

            if self.debug_mode:
                logger.info(f'debug enabled, run "@swallow debug" on {DEV_HOST}.')
            else:
                logger.info("debug disabled.")

        if keyboard.is_pressed("t"):
            self.special_key = False
            self.mode = OperationMode.TRAINING

        if keyboard.is_pressed("g"):
            self.special_key = False
            self.mode = OperationMode.ACTION

        if keyboard.is_pressed("z") and not self.special_key:
            self.special_key = True
            logger.info("🪄 special key enabled.")

        if mode != self.mode:
            logger.info("mode: {}.".format(self.mode.name.lower()))

        if self.special_key:
            for led in self.leds.leds:
                led["state"] = not led["state"]

        return True

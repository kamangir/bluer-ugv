import keyboard

from bluer_options.env import abcli_hostname
from bluer_sbc.session.functions import reply_to_bash

from bluer_ugv.swallow.session.classical.config.classes import ClassicalConfig
from bluer_ugv.swallow.session.classical.controller.classes import ClassicalController
from bluer_ugv.swallow.session.classical.controller.keyboard.keys import ControlKeys
from bluer_ugv.swallow.session.classical.ethernet.classes import ClassicalEthernet
from bluer_ugv.swallow.session.classical.ethernet.command import EthernetCommand
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv import env
from bluer_ugv.logger import logger


class ClassicalKeyboard(ClassicalController):
    def __init__(
        self,
        config: ClassicalConfig,
        ethernet: ClassicalEthernet,
        leds: ClassicalLeds,
        setpoint: ClassicalSetPoint,
    ):
        super().__init__(
            config=config,
            leds=leds,
            setpoint=setpoint,
        )

        self.ethernet = ethernet

        self.keys = ControlKeys()

        self.last_key: str = ""

        self.is_used_for_steering: bool = False

        logger.info(f"created {self.__class__.__name__}")

    def update(self) -> bool:
        self.last_key = ""

        # bash keys
        if self.special_key:
            for key, event in self.keys.special_keys.items():
                if keyboard.is_pressed(key):
                    logger.info(f'*"{key}" is pressed.')

                    if self.ethernet.enabled:
                        self.ethernet.client.send(
                            EthernetCommand(
                                action="keyboard",
                                data={
                                    "sender": abcli_hostname,
                                    "key": key,
                                    "event": event,
                                },
                            ),
                            drain=True,
                        )

                    reply_to_bash(event)
                    return False

        # other keys
        for key, func in {
            self.keys.get("stop"): self.setpoint.stop,
            "x": self.setpoint.start,
            self.keys.get("speed backward"): lambda: self.setpoint.put(
                what="speed",
                value=self.setpoint.get(what="speed") - 10,
            ),
            self.keys.get("speed forward"): lambda: self.setpoint.put(
                what="speed",
                value=self.setpoint.get(what="speed") + 10,
            ),
        }.items():
            if keyboard.is_pressed(key):
                logger.info(f'"{key}" is pressed.')
                self.special_key = False
                func()

        # steering
        if keyboard.is_pressed(self.keys.get("steer left")):
            logger.info('"steer left" is pressed.')
            self.special_key = False
            self.last_key = "a"
            self.setpoint.put(
                what="steering",
                value=env.BLUER_UGV_SWALLOW_STEERING_SETPOINT,
            )

            self.is_used_for_steering = True
        elif keyboard.is_pressed(self.keys.get("steer right")):
            logger.info('"steer right" is pressed.')
            self.special_key = False
            self.last_key = "d"
            self.setpoint.put(
                what="steering",
                value=-env.BLUER_UGV_SWALLOW_STEERING_SETPOINT,
            )

            self.is_used_for_steering = True
        elif self.is_used_for_steering:
            if self.setpoint.check_steering_expiry():
                self.is_used_for_steering = False

        # debug mode
        if keyboard.is_pressed(self.keys.get("debug on")):
            self.set_debug(True)
        if keyboard.is_pressed(self.keys.get("debug off")):
            self.set_debug(False)

        # mode
        mode = self.config.get("mode")
        updated_mode = mode
        if keyboard.is_pressed(self.keys.get("mode = none")):
            updated_mode = OperationMode.NONE

        if keyboard.is_pressed(self.keys.get("mode = action")):
            updated_mode = OperationMode.ACTION

        if keyboard.is_pressed(self.keys.get("mode = training")):
            updated_mode = OperationMode.TRAINING

        if mode != updated_mode:
            self.config.set("mode", updated_mode)
            self.special_key = False

        # ultrasonic
        if keyboard.is_pressed(self.keys.get("ultrasonic off")):
            self.set_ultrasonic(False)
        if keyboard.is_pressed(self.keys.get("ultrasonic on")):
            self.set_ultrasonic(True)

        # special key
        if keyboard.is_pressed(self.keys.get("special key")) and not self.special_key:
            self.set_special_key()

        return super().update()

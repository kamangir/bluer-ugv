import threading
import pygame
from pygame import JOYAXISMOTION, JOYBUTTONDOWN, JOYBUTTONUP, QUIT

from bluer_options.logger import get_logger
from bluer_algo.socket.connection import DEV_HOST
from bluer_sbc.joystick import Joystick
from bluer_sbc.session.functions import reply_to_bash

from bluer_ugv.swallow.session.classical.config import ClassicalConfig
from bluer_ugv.swallow.session.classical.controller.classes import ClassicalController
from bluer_ugv.swallow.session.classical.controller.joystick.controls import Controls
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv import ICON

logger = get_logger(f"{ICON}  🕹️")


class ClassicalJoystick(ClassicalController):
    def __init__(
        self,
        config: ClassicalConfig,
        leds: ClassicalLeds,
        setpoint: ClassicalSetPoint,
    ):
        super().__init__(
            config=config,
            leds=leds,
            setpoint=setpoint,
        )

        self.joystick = Joystick()

        self.controls = Controls

        self.running: bool = False

        if not self.joystick.enabled:
            return

        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def handle_axis(
        self,
        axis: int,
        value: float,
    ):
        if axis in self.controls["axes"]:
            self.special_key = False

            axis_name, axis_direction = self.controls["axes"][axis]
            self.setpoint.put(
                what=axis_name,
                value=axis_direction * int(100 * value),
            )

    def handle_button(self, button: int):
        # bash keys
        if self.special_key:
            if button in self.controls["special-buttons"]:
                event = self.controls["special-buttons"][button]
                logger.info(f'*"{event}" is selected.')
                reply_to_bash(event)
                self.config.set("stop-requested", True)

        if button in self.controls["buttons"]:
            event = self.controls["buttons"][button]

            # ultrasonic
            if event == "ultrasonic off":
                self.set_ultrasonic(False)
            if event == "ultrasonic on":
                self.set_ultrasonic(True)

            # debug
            if event == "debug on":
                self.set_debug(True)
            if event == "debug off":
                self.set_debug(False)

            # mode
            mode = self.config.get("mode")
            updated_mode = mode
            if event == "mode = none":
                updated_mode = OperationMode.NONE

            if event == "mode = action":
                updated_mode = OperationMode.ACTION

            if event == "mode = training":
                updated_mode = OperationMode.TRAINING

            if mode != updated_mode:
                self.config.set("mode", updated_mode)
                self.special_key = False

            # stop
            if event == "stop":
                self.setpoint.stop()
                self.special_key = False

            # special key
            if event == "special key":
                self.set_special_key()

    def loop(self):
        logger.info(f"{self.__class__.__name__}.loop started.")

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    logger.info("QUIT received, and ignored")
                elif event.type == JOYBUTTONDOWN:
                    logger.info(f"button {event.button} pressed.")
                    self.handle_button(event.button)
                elif event.type == JOYBUTTONUP:
                    logger.info(f"button {event.button} released.")
                elif event.type == JOYAXISMOTION:
                    axis = event.axis
                    value = event.value

                    logger.info(f"axis {axis} moved to {value}.")

                    self.handle_axis(
                        axis=axis,
                        value=value,
                    )

            if self.special_key:
                self.leds.flash_all()

            self.joystick.clock.tick(60)

    def stop(self):
        if not self.joystick.enabled:
            return

        self.running = False
        self.thread.join()

        logger.info(f"{self.__class__.__name__} stopped.")

        Joystick.cleanup()

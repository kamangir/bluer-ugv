from typing import Any

from bluer_algo.socket.connection import SocketConnection, DEV_HOST, DEFAULT_PORT
from bluer_sbc.imager.camera import instance as camera

from bluer_ugv.swallow.session.classical.config.classes import ClassicalConfig
from bluer_ugv.swallow.session.classical.controller.keyboard.classes import (
    ClassicalKeyboard,
)
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv.swallow.session.classical.camera.detection import Detection


class ClassicalCamera:
    def __init__(
        self,
        config: ClassicalConfig,
        keyboard: ClassicalKeyboard,
        leds: ClassicalLeds,
        setpoint: ClassicalSetPoint,
        object_name: str,
    ):
        self.config = config
        self.keyboard = keyboard
        self.leds = leds
        self.setpoint = setpoint

        self.detection = Detection()

        self.object_name = object_name

    def initialize(self) -> bool:
        return camera.open(log=True)

    def cleanup(self):
        camera.close(log=True)

    def send_debug_data(
        self,
        data: Any,
        port: int = DEFAULT_PORT,
    ) -> bool:
        socket = SocketConnection.connect_to(
            target_host=DEV_HOST,
            port=port,
        )
        return socket.send_data(data)

    # multi-threaded support
    def stop(self):
        pass

    def update(self) -> bool:
        return True

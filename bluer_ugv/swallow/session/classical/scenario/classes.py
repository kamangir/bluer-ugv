import keyboard
import threading
from typing import Any, Dict

from bluer_options.env import abcli_hostname
from bluer_sbc.session.functions import reply_to_bash
from bluer_algo.socket.connection import DEV_HOST

from bluer_ugv.swallow.session.classical.ethernet.classes import ClassicalEthernet
from bluer_ugv.swallow.session.classical.ethernet.command import EthernetCommand
from bluer_ugv.swallow.session.classical.keyboard.keys import ControlKeys
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv import env
from bluer_ugv.logger import logger


class ClassicalScenario:
    def __init__(
        self,
    ):
        logger.info(self.__class__.__name__)

        self._lock = threading.Lock()
        self.state: Dict[str, Any] = {
            "debug_mode": False,
            "mode": OperationMode.NONE,
            "ultrasound_enabled": True,
        }

    def get(self, what: str, default: Any) -> Any:
        with self._lock:
            return self.state.get(what, default)

    def set(self, what: str, value: Any):
        with self._lock:
            self.state[what] = value

    def update(self) -> bool:
        # TBC
        return True

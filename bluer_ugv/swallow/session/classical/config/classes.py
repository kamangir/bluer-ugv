import threading
from typing import Any, Dict

from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.logger import logger


class ClassicalConfig:
    def __init__(self):
        self._lock = threading.Lock()
        self.config: Dict[str, Any] = {
            "audio_enabled": False,
            "debug_mode": False,
            "ethernet_verbose": False,
            "mode": OperationMode.NONE,
            "ultrasound_enabled": True,
        }

        logger.info(f"🎛️ created {self.as_str()}")

    def as_str(self) -> str:
        with self._lock:
            return "{}[{}]".format(
                self.__class__.__name__,
                ", ".join(
                    [f"{keyword}={value}" for keyword, value in self.config.items()]
                ),
            )

    def get(
        self,
        keyword: str,
        default: Any = None,
    ) -> Any:
        with self._lock:
            return self.config.get(keyword, default)

    def set(
        self,
        keyword: str,
        value: Any,
    ):
        logger.info(f"🎛️ config: {keyword} = {value}")

        with self._lock:
            self.config[keyword] = value

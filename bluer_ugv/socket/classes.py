import socket
import pickle
import struct
from typing import Any, Type, Any, Tuple

from bluer_ugv.logger import logger

DEFAULT_PORT = 8001


class SocketComm:
    def __init__(
        self,
        host: str,
        port: int = DEFAULT_PORT,
    ):
        self.host = host
        self.port = port

        logger.info(
            "created {} {} on {}.".format(
                self.__class__.__name__,
                self.host,
                self.port,
            )
        )

    @classmethod
    def connect_to(
        cls,
        target_host: str,
        port: int = DEFAULT_PORT,
    ) -> "SocketComm":
        return cls(
            host=target_host,
            port=port,
        )

    @classmethod
    def listen_on(
        cls,
        port: int = DEFAULT_PORT,
    ) -> "SocketComm":
        return cls(
            host="0.0.0.0",
            port=port,
        )

    def send_data(self, obj: Any) -> bool:
        """Send any picklable Python object."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                data = pickle.dumps(obj)
                size = struct.pack("!I", len(data))
                s.sendall(size + data)
        except Exception as e:
            logger.error(e)
            return False

        logger.info(f"sent {obj.__class__.__name__}.")
        return True

    def receive_data(self, expected_class: Type) -> Tuple[bool, Any]:
        """Receive a pickled object and check its type."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host, self.port))
                s.listen(1)
                conn, _ = s.accept()
                with conn:
                    data = b""
                    payload_size = struct.calcsize("!I")

                    while len(data) < payload_size:
                        packet = conn.recv(4096)
                        if not packet:
                            return False
                        data += packet

                    packed_size = data[:payload_size]
                    data = data[payload_size:]
                    msg_size = struct.unpack("!I", packed_size)[0]

                    while len(data) < msg_size:
                        packet = conn.recv(4096)
                        if not packet:
                            return False
                        data += packet

                obj = pickle.loads(data[:msg_size])
        except Exception as e:
            logger.error(e)
            return False, None

        if not isinstance(obj, expected_class):
            logger.error(
                "expected {}, got {}".format(
                    expected_class.__name__,
                    obj.__class__.__name__,
                )
            )
            return False, None

        logger.info(f"received {obj.__class__.__name__}.")
        return True, obj

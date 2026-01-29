from typing import Tuple
import threading
import time

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.keyboard.classes import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.ethernet.command import EthernetCommand
from bluer_ugv.swallow.session.classical.ethernet.client import EthernetClient
from bluer_ugv.logger import logger


class ClassicalEthernet:
    def __init__(
        self,
        keyboard: ClassicalKeyboard,
    ):
        is_server: bool = ...
        server_name: str = ""
        ...

        logger.info(
            "creating {}{}...".format(
                self.__class__.__name__,
                " [server]" if is_server else "",
            )
        )
        self.keyboard = keyboard

        self.running = False

        self.client = EthernetClient(
            host="0.0.0.0" if is_server else f"{server_name}.local",
            port=env.BLUER_UGV_ETHERNET_PORT,
            is_server=is_server,
        )

        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

        logger.info(f"{self.__class__.__name__}.stopped.")

        # TODO

    def loop(self):
        logger.info(f"{self.__class__.__name__}.loop started.")

        while self.running:
            connected = self.client._ensure_connection()
            if not connected:
                time.sleep(self.client.reconnect_sec)
                continue

            # 1) receive at most one per tick (cheap + predictable)
            cmd = self.client._try_recv_one()
            if cmd is not None:
                self.client._recv_q.put(cmd)

            # 2) drain outbound queue
            self.client._drain_send_queue()

            time.sleep(0.1)

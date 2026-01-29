import threading
import time

from bluer_options.env import abcli_hostname

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.keyboard.classes import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.ethernet.client import EthernetClient
from bluer_ugv.README.ugvs.ethernet import find_server
from bluer_ugv.logger import logger


class ClassicalEthernet:
    def __init__(
        self,
        keyboard: ClassicalKeyboard,
    ):
        self.enabled: bool = True

        logger.info(f"creating {self.__class__.__name__}...")

        self.keyboard = keyboard

        self.running = False

        self.enabled, is_server, server_name = find_server(hostname=abcli_hostname)
        if not self.enabled:
            return

        self.client = EthernetClient(
            host=server_name,
            port=env.BLUER_UGV_ETHERNET_PORT,
            is_server=is_server,
        )

        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def stop(self):
        if not self.enabled:
            return

        self.running = False
        self.thread.join()

        self.client._close_sockets()
        logger.info(f"{self.__class__.__name__}.stopped.")

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

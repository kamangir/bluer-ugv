from typing import Any, Type

from blueness import module

from bluer_ugv import NAME
from bluer_ugv.socket.classes import SocketComm
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


def test_receiving(expected_class: Type = str) -> bool:
    logger.info(f"{NAME}: testing receiving ...")

    socket = SocketComm.listen_on()

    success, data = socket.receive_data(expected_class)
    if not success:
        return success

    logger.info(f"received {data}")
    print(data)
    return True


def test_sending(
    target_host: str,
    data: Any = "hello-world",
) -> bool:
    logger.info(f"{NAME}: testing sending ...")

    socket = SocketComm.connect_to(target_host)

    return socket.send_data(data)

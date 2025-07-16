from blueness import module
import numpy as np

from bluer_algo.socket.classes import SocketComm

from bluer_ugv import NAME
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def select_target(host: str) -> bool:
    logger.info(f"{NAME}.select_target on {host}")

    socket = SocketComm.listen_on()

    success, data = socket.receive_data(np.ndarray)
    if not success:
        return success

    import ipdb

    ipdb.set_trace()

    return True

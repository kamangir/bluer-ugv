from blueness import module
import numpy as np

from bluer_algo.socket.classes import SocketComm
from bluer_algo.tracker.classes.target import Target

from bluer_ugv import NAME
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def select_target(host: str) -> bool:
    logger.info(f"{NAME}.select_target on {host}")

    socket = SocketComm.listen_on()
    success, image = socket.receive_data(np.ndarray)
    if not success:
        return success

    success, track_window = Target.select(image)
    if not success:
        return success

    socket = SocketComm.connect_to(host)
    return socket.send_data(track_window)

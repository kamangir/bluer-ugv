from blueness import module
import numpy as np
import cv2

from bluer_options.terminal import hr
from bluer_algo.socket.classes import SocketComm
from bluer_algo.tracker.classes.target import Target

from bluer_ugv import NAME
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def debug(
    host: str,
    loop: bool = True,
) -> bool:
    logger.info(
        "{}.debug on {}{}".format(
            NAME,
            host,
            " on a loop." if loop else "",
        )
    )

    socket = SocketComm.listen_on()

    cv2.namedWindow(host)
    logger.info(f"Ctrl+C to exit...")

    try:
        while loop:
            success, image = socket.receive_data(np.ndarray)
            if not success:
                break

            cv2.imshow(host, image)
            cv2.waitKey(1)
    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")

    cv2.destroyWindow(host)

    return True

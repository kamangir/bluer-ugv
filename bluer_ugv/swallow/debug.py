from blueness import module
import numpy as np
import cv2
from typing import List

from bluer_options import string
from bluer_objects import file
from bluer_objects import objects
from bluer_objects.graphics.gif import generate_animated_gif
from bluer_algo.socket.connection import SocketConnection
from bluer_algo.socket.message import SocketMessage

from bluer_ugv import NAME
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def debug(
    object_name: str,
    generate_gif: bool = True,
    save_images: bool = True,
) -> bool:
    logger.info(
        "{}.debug -{}{}> {}".format(
            NAME,
            "images-" if save_images else "",
            "gif-" if generate_gif else "",
            object_name,
        )
    )

    socket = SocketConnection.listen_on()

    title = "debug..."

    cv2.namedWindow(title)
    logger.info("Ctrl+C to exit...")

    image = np.zeros((480, 640, 3), np.uint8)

    list_of_images: List[str] = []
    try:
        while True:
            cv2.imshow(title, np.flip(image, axis=2))
            cv2.waitKey(1)

            success, message = socket.receive_data(SocketMessage)
            if not success:
                break

            assert isinstance(message, SocketMessage)

            logger.info(f"message from {message.hostname}.")

            image = message.payload.get("image", image)

            if save_images:
                filename = objects.path_of(
                    filename="{}.png".format(string.timestamp()),
                    object_name=object_name,
                )

                if not file.save_image(filename, image, log=True):
                    break

                list_of_images.append(filename)
    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")

    cv2.destroyWindow(title)

    if generate_gif:
        if not generate_animated_gif(
            list_of_images,
            objects.path_of(
                filename=f"{object_name}.gif",
                object_name=object_name,
            ),
        ):
            return False

    return True

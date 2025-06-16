from bluer_ugv.swallow.session.classical.mousepad import ClassicalMousePad
from bluer_ugv.logger import logger


class GenericMotor:
    def __init__(
        self,
        role: str,
        mousepad: ClassicalMousePad,
    ):
        self.role = role
        self.mousepad = mousepad

        logger.info(
            "{}: {}".format(
                self.__class__.__name,
                role,
            )
        )

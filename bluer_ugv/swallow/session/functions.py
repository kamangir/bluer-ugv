import time
from RPi import GPIO  # type: ignore

from blueness import module

from bluer_ugv import NAME
from bluer_ugv.swallow.session.classical.session import ClassicalSession
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


def start_session() -> bool:
    logger.info(f"{NAME}.start_session.")

    session = ClassicalSession()

    if not session.initialize():
        return False

    try:
        while not (session.button_command() or session.key_command()):
            session.leds.update()
            time.sleep(0.05)
    except KeyboardInterrupt:
        logger.info("^C received.")
        return False
    finally:
        logger.info("GPIO.cleanup...")
        GPIO.cleanup()

    return True

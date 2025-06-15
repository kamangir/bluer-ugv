from RPi import GPIO  # type: ignore

from bluer_ugv.logger import logger


class ClassicalLeds:
    def __init__(self):
        self.leds = {
            "yellow": {"pin": 17, "state": True},
            "red": {"pin": 27, "state": False},
            "green": {"pin": 22, "state": True},
        }

    def initialize(self) -> bool:
        try:
            for led in self.leds.values():
                GPIO.setup(
                    led["pin"],
                    GPIO.OUT,
                )
        except Exception as e:
            logger.error(e)
            return False

        return True

    def update(self):
        self.leds["green"]["state"] = not self.leds["green"]["state"]

        for led in self.leds.values():
            GPIO.output(
                led["pin"],
                GPIO.HIGH if led["state"] else GPIO.LOW,
            )

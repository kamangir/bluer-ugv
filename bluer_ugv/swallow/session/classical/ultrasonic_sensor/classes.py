from RPi import GPIO

from bluer_ugv.logger import logger


class ClassicalUltrasonicSensor:
    def __init__(
        self,
        side: str,
        setmode: bool = True,
    ):
        self.side = side
        self.valid = True

        # Pin definitions
        if side == "left":
            self.TRIG = 23  # GPIO 23, pin 16
            self.ECHO = 24  # GPIO 24, pin 18
        elif side == "right":  # right
            self.TRIG = 5  # GPIO 5,  pin 29
            self.ECHO = 25  # GPIO 25, pin 22
        else:
            logger.error(f"{side}: ultrasonic sensor not found.")
            self.valid = False

        if not self.valid:
            return

        if setmode:
            GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.TRIG, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        logger.info(
            "{}: {} ultrasonic sensor initialized on TRIG=GPIO#{}, ECHO=GPIO#{}".format(
                self.__class__.__name__,
                self.side,
                self.TRIG,
                self.ECHO,
            )
        )

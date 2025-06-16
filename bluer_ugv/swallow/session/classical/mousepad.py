import evdev  # type: ignore
from evdev import InputDevice, categorize, ecodes, list_devices  # type: ignore
import threading

from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.logger import logger


class ClassicalMousePad:
    def __init__(self, leds: ClassicalLeds):
        self.speed = 0
        self.steering = 0

        self.started = False

        self.leds = leds

        try:
            self.device = InputDevice("/dev/input/event0")
            logger.info(
                "{}: using {}.".format(
                    self.__class__.__name__,
                    self.device.name,
                )
            )
        except Exception as e:
            logger.warning(e)
            self.device = None
            return

        self._thread = threading.Thread(
            target=self.run_,
            daemon=True,
        )
        self._thread.start()

    def run_(self) -> bool:
        logger.info(f"{self.__class__.__name__}: thread started.")
        for event in self.device.read_loop():
            if event.type == ecodes.EV_REL:
                if event.code == ecodes.REL_Y:
                    if self.started:
                        self.speed -= event.value  # up/down
                        self.speed = min(255, max(-255, self.speed))
                elif event.code == ecodes.REL_X:
                    self.steering = event.value  # left/right
                    self.steering = min(255, max(-255, self.steering))

                logger.info(f"speed: {self.speed}, steering: {self.steering}")
                self.leds.leds["yellow"]["state"] = not self.leds.leds["yellow"][
                    "state"
                ]

            # Optional: reset on button release
            elif (
                event.type == ecodes.EV_KEY
                and event.code == ecodes.BTN_LEFT
                and event.value == 0
            ):
                self.stop()

            if self.started:
                self.leds.leds["red"]["state"] = not self.leds.leds["red"]["state"]

        return True

    def start(self):
        self.speed = 0
        self.steering = 0
        self.started = True

        logger.info("started")

    def stop(self):
        self.speed = 0
        self.steering = 0
        self.started = False

        logger.info("stopped")

        self.leds.leds["red"]["state"] = False
        self.leds.leds["yellow"]["state"] = False

    def get_state(self):
        return self.speed, self.steering

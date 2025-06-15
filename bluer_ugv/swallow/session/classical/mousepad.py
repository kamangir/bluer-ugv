import evdev  # type: ignore
from evdev import InputDevice, categorize, ecodes, list_devices  # type: ignore
import threading

from bluer_ugv.swallow.session.classical.led import ClassicalLeds
from bluer_ugv.logger import logger


class ClassicalMousePad:
    def __init__(self, leds: ClassicalLeds):
        self.device = InputDevice("/dev/input/event0")
        logger.info(
            "{}: using {}.".format(
                self.__class__.__name__,
                self.device.name,
            )
        )

        self.speed = 0
        self.steering = 0

        self.leds = leds

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
                    self.speed -= event.value  # up/down
                elif event.code == ecodes.REL_X:
                    self.steering += event.value  # left/right

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
                self.speed = 0
                self.steering = 0

                logger.info("stopped")
                self.leds.leds["yellow"]["state"] = False

        return True

    def get_state(self):
        return self.speed, self.steering

import evdev  # type: ignore
from evdev import InputDevice, categorize, ecodes, list_devices  # type: ignore


class ClassicalMousePad:
    def check(self) -> bool:
        # List all input devices
        devices = [InputDevice(path) for path in list_devices()]

        print("Available input devices:")
        for device in devices:
            print(f"  {device.path}: {device.name}")
            caps = device.capabilities()

            has_abs = ecodes.EV_ABS in caps
            has_touch = (
                ecodes.EV_KEY in caps and ecodes.BTN_TOUCH in caps[ecodes.EV_KEY]
            )

            abs_info = caps[ecodes.EV_ABS] if has_abs else []
            abs_axes = [ecodes.ABS[code] for code, *_ in abs_info] if has_abs else []

            logger.info(
                "Has ABS_X/ABS_Y: {}".format(
                    "ABS_X" in abs_axes and "ABS_Y" in abs_axes
                )
            )
            logger.info(f"Has BTN_TOUCH: {has_touch}")

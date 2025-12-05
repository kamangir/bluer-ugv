title:::

- [test the shield](./shield/testing.md).
- disconnect the shield from the [XL4015](https://github.com/kamangir/bluer-sbc/blob/main/bluer_sbc/docs/parts/XL4015.md) and connect the computer to the [battery bus](https://github.com/kamangir/bluer-sbc/blob/main/bluer_sbc/docs/battery_bus). validate that the red LED on the XL4015 turns on.
- adjust XL4015 at 5.1 V.
- separate the shield from the rpi, connect power to the shield, turn the power on, validate no 💥, turn the power off.
- install the shield on the rpi, screw the shield, connect the monitor (for rpi4b: to the hdmi port closer to the USB port) and the keyboard, turn the power on, validate full operation, shutdown, power off.
- wire the ultrasonic sensors, turn the power on, validate that ultrasonic sensors log warning and danger, `@swallow debug`, test the camera, shutdown, power off.

items:::
# swallow: digital: design: computer: testing

- [test the shield](./shield/testing.md).
- disconnect the shield from the [XL4015](../../../../../../../bluer-sbc/bluer_sbc/docs/parts/XL4015.md) and connect the computer to the [battery bus](../../../../../../../bluer-sbc/bluer_sbc/docs/battery_bus) or [adapter bus](../../../../../../../bluer-sbc/bluer_sbc/docs/adapter_bus.md). validate that the red LED on the XL4015 turns on.
- adjust XL4015 at 5.1 VDC.
- separate the shield from the rpi, connect power to the shield, turn the power on, validate no 💥, validate that the output of XL-4015 is ~5.1 VDC, turn the power off.
- attach a 5 Ω resistor to the outputs of XL4015 and validate that output stays ~5.1 VDC.
- install the shield on the rpi, screw the shield, connect the monitor (for rpi4b: to the hdmi port closer to the USB port) and the keyboard, turn the power on, validate full operation, shutdown, power off.
- wire the ultrasonic sensors, turn the power on, validate that ultrasonic sensors log warning and danger, `@swallow debug`, test the camera, shutdown, power off.

|   |   |   |
| --- | --- | --- |
| [![image](../../../../../../../assets2/swallow/20251116_145939.jpg?raw=true)](../../../../../../../assets2/swallow/20251116_145939.jpg?raw=true) | [![image](../../../../../../../assets2/swallow/20251116_150940.jpg?raw=true)](../../../../../../../assets2/swallow/20251116_150940.jpg?raw=true) | [![image](../../../../../../../assets2/swallow/20251116_151611.jpg?raw=true)](../../../../../../../assets2/swallow/20251116_151611.jpg?raw=true) |
| [![image](../../../../../../../assets2/swallow/20251116_152801.jpg?raw=true)](../../../../../../../assets2/swallow/20251116_152801.jpg?raw=true) | [![image](../../../../../../../assets2/swallow/20251116_152832_1.gif?raw=true)](../../../../../../../assets2/swallow/20251116_152832_1.gif?raw=true) | [![image](../../../../../../../assets2/swallow/2026-01-25-12-21.jpg?raw=true)](../../../../../../../assets2/swallow/2026-01-25-12-21.jpg?raw=true) |
| [![image](../../../../../../../assets2/swallow/2026-01-25-12-16.jpg?raw=true)](../../../../../../../assets2/swallow/2026-01-25-12-16.jpg?raw=true) |  |  |

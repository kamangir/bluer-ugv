# [Bluer Swallow](./bluer-swallow.md): Digital Control: Parts

- Raspberry Pi 3B+
- DC motors: 12 VDC, 20-45 W, 9000 RPM
- Battery: Rechargeable sealed lead acid, 12 V, 7 Ah
- DC 12 VDC -> 5 VDC, 4A: [XL4015](https://www.handsontec.com/dataspecs/module/XL4015-5A-PS.pdf)
- Rear drive (2 motors) & Steering drive (1 motor): [BTS7960](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf)
- Capacitor: 470 μF to 1000 μF, 16 V or 25 V, Electrolytic, 105 °C rated if possible.
- Polyfuse: 1.1 A hold, 2.2 A trip, 16 V, resettable, through-hole, e.g., MF-R110
- TVS diode, unidirectional, 600 W, 6.8 V clamp, e.g. P6KE6.8A, DO-15 package
- Resistor, 330–470 Ω, 1/4 watt, 5% tolerance
- LED, ~2 V forward voltage, 10–20 mA

## rpi pinout 🔥

| Responsibility | Function  | Physical Pin | GPIO #  | Notes                                      |
| -------------- | --------- | ------------ | ------- | ------------------------------------------ |
| Steering Motor | PWM Right | 12           | GPIO 18 | PWM0                                       |
| Steering Motor | PWM Left  | 32           | GPIO 12 | PWM0 (alternate), Shares PWM0 with GPIO 18 |
| Rear Motors    | PWM Right | 33           | GPIO 13 | PWM1                                       |
| Rear Motors    | PWM Left  | 35           | GPIO 19 | PWM1 (alternate), Shares PWM1 with GPIO 13 |
| Green LED      |           | 11           | GPIO 17 |                                            |
| RED LED        |           | 13           | GPIO 27 |                                            |
| Blue LED       |           | 15           | GPIO 22 |                                            |

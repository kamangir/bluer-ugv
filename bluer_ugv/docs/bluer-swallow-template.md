# Bluer Light

| | | |
|-|-|-|
| ![image](../../diagrams/bluer-swallow/3d-design.png) | ![image](https://github.com/kamangir/assets2/blob/main/bluer-swallow/20250605_180136.jpg?raw=true) | ![image](https://github.com/kamangir/assets2/blob/main/bluer-swallow/20250608_144453.jpg?raw=true) |

based on power wheels, sources:

- https://persian-toys.com/
- https://www.instagram.com/khamooshi_bike

## diagram

- [3d-design](../../diagrams/bluer-swallow/3d-design.stl)
- [electrical](../../diagrams/bluer-swallow/electrical.svg)
- [automation](../../diagrams/bluer-swallow/automation.svg)

## parts

- DC motors: 12 VDC, 20-45 W, 9000 RPM
- Battery: 12 V, 7 Ah
- DC 12 VDC -Buck Converter-> 5 VDC, 4A: [XL4015](https://www.handsontec.com/dataspecs/module/XL4015-5A-PS.pdf)
- Rear drive (2 motors) & Steering drive (1 motor): [BTS7960](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf)
- male header
- prototyping wires 
- prototype board 

| Driver         | Max Current | PWM+2 DIR    | Logic Level             | Best For                  |
| -------------- | ----------- | ------------ | ----------------------- | ------------------------- |
| L298N          | 2A          | ✅           | 5V (needs level shift)  | Steering (light load)     |
| MD10C (Cytron) | 10A         | ✅ (PWM+DIR) | 3.3V native             | Rear motors (in parallel) |
| Monster Moto   | \~7A        | ✅           | 5V (may work with 3.3V) | Rear or steering          |
| Pololu G2      | 13–17A+     | ✅           | 3.3V compatible         | Any motor (robust)        |


## pinout 🔥

| Motor          | Function      | GPIO Pin     | Notes                |
| -------------- | ------------- | ------------ | -------------------- |
| Rear Motors    | PWM           | GPIO18       | Hardware PWM0 (ALT5) |
| Rear Motors    | Direction IN1 | GPIO23       |                      |
| Rear Motors    | Direction IN2 | GPIO24       |                      |
| Steering Motor | PWM           | GPIO13       | Hardware PWM1 (ALT0) |
| Steering Motor | Direction IN1 | GPIO27       |                      |
| Steering Motor | Direction IN2 | GPIO22       |                      |


## comments

- [ ] RPi digital in/outputs operate at 3.3 VDC 🔥
- [ ] adjust the RPi voltage to 5.1 VDC 🔥
- [ ] connect the grounds (the 12V battery, the buck converter, the motor driver, and RPi)  🔥
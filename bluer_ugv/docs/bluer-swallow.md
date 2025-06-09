# Bluer Light

|   |   |   |
| --- | --- | --- |
| [![image](https://github.com/kamangir/assets/blob/main/bluer-ugv/bluer-fire.png?raw=true)](https://github.com/kamangir/assets/blob/main/bluer-ugv/bluer-fire.png?raw=true) | [![image](../../diagrams/bluer-swallow/3d-design.png)](../../diagrams/bluer-swallow/3d-design.stl) | [![image](https://github.com/kamangir/assets2/blob/main/bluer-swallow/20250605_180136.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/bluer-swallow/20250605_180136.jpg?raw=true) |
| [![image](https://github.com/kamangir/assets2/blob/main/bluer-swallow/20250608_144453.jpg?raw=true)](https://github.com/kamangir/assets2/blob/main/bluer-swallow/20250608_144453.jpg?raw=true) |  |  |

based on power wheels, sources:

- https://persian-toys.com/
- https://www.instagram.com/khamooshi_bike

## diagrams

- [analog](../../diagrams/bluer-swallow/analog.svg)
- [digital](../../diagrams/bluer-swallow/automation.svg)

## digital parts

- DC motors: 12 VDC, 20-45 W, 9000 RPM
- Battery: 12 V, 7 Ah
- DC 12 VDC -Buck Converter-> 5 VDC, 4A: [XL4015](https://www.handsontec.com/dataspecs/module/XL4015-5A-PS.pdf)
- Rear drive (2 motors) & Steering drive (1 motor): [BTS7960](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf)
- male header
- prototyping wires 
- prototype board 

## rpi pinout 🔥

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

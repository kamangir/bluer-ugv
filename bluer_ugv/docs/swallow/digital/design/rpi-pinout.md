# swallow: digital: design: rpi-pinout

| Responsibility        | Function       | Physical Pin | GPIO | Notes                                      |
| --------------------- | -------------- | ------------ | ---- | ------------------------------------------ |
| Motor 1, FW           | PWM            | 12           | 18   | PWM0, Steering / Right                     |
| Motor 1, BW           | PWM            | 32           | 12   | PWM0 (alternate), Shares PWM0 with GPIO 18 |
| Motor 2, FW           | PWM            | 33           | 13   | PWM1, Rear / Left                          |
| Motor 2, BW           | PWM            | 35           | 19   | PWM1 (alternate), Shares PWM1 with GPIO 13 |
| Green LED             | Digital Output | 11           | 17   |                                            |
| RED LED               | Digital Output | 13           | 27   |                                            |
| Blue LED              | Digital Output | 15           | 22   |                                            |
| Push Button           | Digital Input  | 37           | 26   |                                            |
| Sensor 1, Trigger     | Digital Output | 16           | 23   |                                            |
| Sensor 2, Trigger     | Digital Output | 29           | 5    |                                            |
| Sensor 3, Trigger     | Digital Output | 31           | 6    |                                            |
| Sensor 4, Trigger     | Digital Output | 36           | 16   |                                            |
| Sensor 1, Echo        | Digital Input  | 18           | 24   |                                            |
| Sensor 2, Echo        | Digital Input  | 22           | 25   |                                            |
| Sensor 3, Echo        | Digital Input  | 38           | 20   |                                            |
| Sensor 4, Echo        | Digital Input  | 40           | 21   |                                            |


# [Bluer Swallow](./bluer-swallow.md): Digital Control: Raspberry Pi Pin-Out

| Responsibility | Function  | Physical Pin | GPIO #  | Notes                                      |
| -------------- | --------- | ------------ | ------- | ------------------------------------------ |
| Steering Motor | PWM Right | 12           | GPIO 18 | PWM0                                       |
| Steering Motor | PWM Left  | 32           | GPIO 12 | PWM0 (alternate), Shares PWM0 with GPIO 18 |
| Rear Motors    | PWM Right | 33           | GPIO 13 | PWM1                                       |
| Rear Motors    | PWM Left  | 35           | GPIO 19 | PWM1 (alternate), Shares PWM1 with GPIO 13 |
| Green LED      |           | 11           | GPIO 17 |                                            |
| RED LED        |           | 13           | GPIO 27 |                                            |
| Blue LED       |           | 15           | GPIO 22 |                                            |

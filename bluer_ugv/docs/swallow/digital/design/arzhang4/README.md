# swallow: digital: design: arzhang4

[arzhang](../../../../arzhang) with external motors.



## design

Objective: To build an unmanned ground vehicle (UGV) with scooter or electric bike motorized wheels.

> Do these wheels, and their drivers, support going backward?

- Motor: almost always physically capable of reverse.
- Driver/controller: sometimes supports reverse, sometimes needs enabling, sometimes doesn’t exist.

> Key factors in motor + driver:

- Reverse input
- Brake input
- Current limiting
- optional: encoder feedback

## parts

|   |   |   |
| --- | --- | --- |
| [`300 W industrial brushless motor driver.`](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/brushless-driver.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/brushless-driver-1.jpg?raw=true)](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/brushless-driver.md) 4 x | [`Rechargeable sealed lead acid battery`](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/SLA-Battery.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/battery.png?raw=true)](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/SLA-Battery.md) 12 V, 42 Ah, 185 mm x 150 mm x 175 mm | [`scooter wheel, 36 V, 300 W, 650 rpm, 10"`](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/scooter-wheel.md) [![image](https://github.com/kamangir/assets2/raw/main/bluer-sbc/parts/scooter-wheel-1.jpg?raw=true)](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/scooter-wheel.md) 4 x |

1. [300 W industrial brushless motor driver.](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/brushless-driver.md): 4 x.
1. [Rechargeable sealed lead acid battery](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/SLA-Battery.md): 12 V, 42 Ah, 185 mm x 150 mm x 175 mm.
1. [scooter wheel, 36 V, 300 W, 650 rpm, 10"](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/parts/scooter-wheel.md): 4 x.

> 650 rpm @ 10 inch radius wheel == 650 / 60 * 25.4 * 3.14 / 100 = 8.64 m /s == 31.1 km / h ⭐️

🔋 total power: 1200 W ~= 100 A at 12 V -> 42 AH battery.

---

- [v1](./v1.md)

title:::

tagline:::

set:::object_name arzhang4-design-v1

ai:::object get:::object_name

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

parts_images:::

parts_list:::

> 650 rpm @ 10 inch radius wheel == 650 / 60 * 25.4 * 3.14 / 100 = 8.64 m /s == 31.1 km / h ⭐️

🔋 total power: 1200 W ~= 100 A at 12 V -> 42 AH battery.

---

- [v1](./v1.md)
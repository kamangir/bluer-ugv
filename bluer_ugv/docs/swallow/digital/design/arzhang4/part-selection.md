# swallow: digital: design: arzhang4: part-selection

Objective: To build an unmanned ground vehicle (UGV) with scooter or electric bike motorized wheels.

> Do these wheels, and their drivers, support going backward?

- Motor: almost always physically capable of reverse.
- Driver/controller: sometimes supports reverse, sometimes needs enabling, sometimes doesn’t exist.

> Key factors in motor + driver:

- Reverse input
- Brake input
- Current limiting
- optional: encoder feedback

🔋 total power: 1200 W ~= 100 A at 12 V -> 42 AH battery.

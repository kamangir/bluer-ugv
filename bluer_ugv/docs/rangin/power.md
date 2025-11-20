# rangin: power

- uses [swallow computer power](./../swallow/digital/design/computer/power.md).
   - swallow: 60 W
   - 3 x swallow-head: 3 x 10 W = 30 W @ 12 V DC
- 2 x [40 inch TVs](https://github.com/kamangir/bluer-sbc/blob/main/bluer_sbc/docs/parts/TV.md): 2 x 0.2-0.5 A @ 220 V AC = 88 - 220 W @ 220 V AC -80%-90% efficiency of power inverter-> 100 - 260 W @ 12 V DC ~= 9 - 22 A
- total: 300 W ~= 25 A @ 12 V DC

| runtime | energy needed | ideal capacity @12 V | SLA nominal Ah | LiPo nominal Ah |
|-|-|-|-|-|
| 1 h | 300 Wh | 25 Ah | 30 Ah | 30 Ah |
| 2 h | 600 Wh | 50 Ah | 60 Ah | 60 Ah |
| 3 h | 900 Wh | 75 Ah | 90 Ah | 85–90 Ah |
| 4 h | 1200 Wh | 100 Ah | 120 Ah | 120 Ah |
| 5 h | 1500 Wh | 125 Ah | 150 Ah | 140–150 Ah |

> SLA: 85%

> LiPo: 90%


|   |
| --- |
| [![image](https://github.com/kamangir/bluer-designs//blob/main/rangin/electrical/electrical.png?raw=true)](https://github.com/kamangir/bluer-designs//blob/main/rangin/electrical/electrical.svg) |

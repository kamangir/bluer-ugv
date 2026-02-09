# rangin: power

- uses [swallow computer power](../../swallow/digital/design/computer/power.md).
   - swallow + swallow-top: 120 W
- [40 inch TVs](../../../../../bluer-sbc/bluer_sbc/docs/parts/TV.md): 0.2-0.5 A @ 220 V AC = 44 - 110 W @ 220 V AC -80%-90% efficiency of power inverter-> 50 - 130 W @ 12 V DC ~= 4.5 - 11 A
- total: 250 W ~= 20 A @ 12 V DC

| runtime | energy needed | ideal capacity @12 V | SLA nominal Ah | LiPo nominal Ah |
|-|-|-|-|-|
| 1 h | 250 Wh | 20 Ah | 25 Ah | 25 Ah |
| 2 h | 500 Wh | 40 Ah | 50 Ah | 50 Ah ⭐️ |
| 3 h | 750 Wh | 60 Ah | 75 Ah | 75 Ah |
| 4 h | 1000 Wh | 80 Ah | 100 Ah | 100 Ah |
| 5 h | 1250 Wh | 100 Ah | 125 Ah | 125 Ah |

> SLA: 85%, LiPo: 90%

- previous design(s): [v1](./v1.md).

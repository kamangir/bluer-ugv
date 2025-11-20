# swallow: digital: design: computer: power

[swallow head](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/swallow-head):
- Raspberry Pi 4B (CPU/GPU busy, Wi-Fi + BLE on): ~ 1.3–1.5 A -> ~ 6.6–7.7 W
- Raspberry Pi Camera (capturing video): ~ 200–250 mA -> ~ 1.0–1.3 W
- 4 × HC-SR04 (all active): ~ 15 mA each → ~ 60 mA -> ~ 0.3 W
- HDMI connection: ~ 50 mA -> 0.25 W

total: ~ 10 W ~= ~1.8 A @ 5.1 V DC ~= 1 A @ 12 V DC (90% efficiency)

[swallow](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/swallow): 
- 4 x BTS7960 logic side: ~ 10–20 mA -> 0.1 W (will consider included in ⬆️)
- 4 x DC motors: 1 A (freely-rotating) - 4 A (stalled) ~= 8 A -> ~ 100 W

total: 110 W - max current: 15 A @ 12 V DC

| option | battery | rated Wh | usable Wh | aggressive Driving | cruising driving | mostly idling |
|-|-|-|-|-|-|-|
| | | | | ~107 W == ~9 A | ~59 W == ~ 5A | 12 W == ~ 1 A |
| SLA | | | | | | |
| 1 | 7.2 Ah ⭐️ | 86 Wh | 50–65 Wh | 28–37 min | 50–70 min | 4–5.5 h |
| 2 | 12 Ah | 144 Wh | 85–110 Wh | 48–62 min | 1.4–1.8 h | 7–9 h |
| 3 | 18 Ah | 216 Wh | 130–165 Wh | 73–92 min | 2.2–2.8 h | 11–14 h |
| 4 | 20 Ah | 240 Wh | 145–180 Wh | 81–100 min | 2.5–3.0 h | 12–15 h |
| 5 | 30 Ah | 360 Wh | 215–270 Wh | 2.0–2.5 h | 3.6–4.6 h | 18–22 h |
| LiPo | | | | | | |
| 6 | 7 Ah | 78 Wh | 66 Wh | 0.62 h | 1.12 h | 33.0 h |
| 7 | 10 Ah | 111 Wh | 94 Wh | 0.88 h | 1.60 h | 47.2 h |
| 8 | 15 Ah | 166 Wh | 142 Wh | 1.32 h | 2.40 h | 70.8 h |
| 9 | 20 Ah | 222 Wh | 189 Wh | 1.76 h | 3.20 h | 94.3 h |
| 10 | 25 Ah | 278 Wh | 236 Wh | 2.20 h | 4.00 h | 117.9 h |
| 11 | 30 Ah | 333 Wh | 283 Wh | 2.65 h | 4.80 h | 141.5 h |


> SLA: 12 V, 60–75% usable capacity.

> LiPo: 3S, 11.1 V nominal, 85% usable capacity.






|   |   |
| --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193930.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193930.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193954.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193954.jpg?raw=true) |

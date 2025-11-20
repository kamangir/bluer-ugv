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

| Battery | Rated Wh | Usable Wh | Aggressive Driving | Cruising Driving | Mostly Idling |
| 12 V SLA |  | real | ~107 W == ~9 A | ~59 W == ~ 5A | 12 W == ~ 1 A |
|-|-|-|-|-|-|
| 7.2 Ah ⭐️ | 86 Wh | 50–65 Wh | 28–37 min | 50–70 min | 4–5.5 h |
| 12 Ah | 144 Wh | 85–110 Wh | 48–62 min | 1.4–1.8 h | 7–9 h |
| 18 Ah | 216 Wh | 130–165 Wh | 73–92 min | 2.2–2.8 h | 11–14 h |
| 20 Ah | 240 Wh | 145–180 Wh | 81–100 min | 2.5–3.0 h | 12–15 h |
| 30 Ah | 360 Wh | 215–270 Wh | 2.0–2.5 h | 3.6–4.6 h | 18–22 h |


|   |   |
| --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193930.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193930.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193954.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193954.jpg?raw=true) |

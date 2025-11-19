# swallow: digital: design: shield: power

[swallow head](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/swallow-head):
- Raspberry Pi 4B (CPU/GPU busy, Wi-Fi + BLE on): ~ 1.3–1.5 A -> ~ 6.6–7.7 W
- Raspberry Pi Camera (capturing video): ~ 200–250 mA -> ~ 1.0–1.3 W
- 4 × HC-SR04 (all active): ~ 15 mA each → ~ 60 mA -> ~ 0.3 W

total: ~ 10 W ~= ~1.8 A @ 5.1 V DC ~= 1 A @ 12 V DC (90% efficiency)

[swallow](https://github.com/kamangir/bluer-sbc/tree/main/bluer_sbc/docs/swallow): 
- 4 x BTS7960 logic side: ~ 10–20 mA -> 0.1 W (will consider included in ⬆️)
- 4 x DC motors: 1 A (freely-rotating) - 4 A (stalled) ~= 8 A -> ~ 100 W

total: 110 W - max current: 15 A @ 12 V DC

|   |   |
| --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193930.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193930.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193954.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251119_193954.jpg?raw=true) |

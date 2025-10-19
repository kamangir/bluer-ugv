title:::

UGV(s): ugv_name:::

## scripts

```bash
@select swallow-debug-2025-10-19-14-14-23-ectn97

@upload public,zip

@assets publish extensions=gif,push
```
set:::debug_object swallow-debug-2025-10-19-14-14-23-ectn97

```bash
runme() {
    @select $1

    @swallow ultrasonic review \
    	upload .    

    @assets publish extensions=gif+png,push
}

runme 2025-10-19-14-16-36-tunrlm
runme 2025-10-19-14-16-07-75yxbw
```

set:::arzhang1_object 2025-10-19-14-16-36-tunrlm
set:::arzhang2_object 2025-10-19-14-16-07-75yxbw

## objects

### arzhang

loop frequency (Hz): metadata:::get:::arzhang1_object:::loop_frequency

### arzhang2

loop frequency (Hz): metadata:::get:::arzhang2_object:::loop_frequency

---

| [arzhang](../../UGVs/arzhang.md) | [arzhang2](../../UGVs/arzhang2.md) |
|-|-|
| assets:::get:::arzhang1_object | assets:::get:::arzhang2_object |
| assets:::get:::arzhang1_object/ultrasonic-sensor-detections.gif | assets:::get:::arzhang2_object/ultrasonic-sensor-detections.gif |
| assets:::get:::arzhang1_object/ultrasonic-sensor-state.png | assets:::get:::arzhang2_object/ultrasonic-sensor-state.png |
| assets:::get:::arzhang1_object/ultrasonic-sensor-distance-mm.png | assets:::get:::arzhang2_object/ultrasonic-sensor-distance-mm.png |

assets:::get:::debug_object/get:::arzhang1_debug_object.gif

## observations

- the range of numpad is ~10-20 m range, noticeably lower than that of the full keyboard, which is ~50 m. 

---

items:::
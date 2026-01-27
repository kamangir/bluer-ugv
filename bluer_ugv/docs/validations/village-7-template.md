title:::

ugv_name:::

set:::arzhang1_object 2025-11-06-10-50-35-myadvn
set:::arzhang2_object 2025-11-06-10-49-58-denev4
set:::arzhang3_object 2025-11-06-10-49-36-koxzf3

details:::publication
```bash
@ls cloud,objects --prefix 2025-11-06
```

```bash
runme() {
    local object_name
    for object_name in \
        get:::arzhang1_object \
        get:::arzhang2_object \
        get:::arzhang3_object; do
        @select $object_name
        @assets publish extensions=gif+png,push
        @upload public,zip
    done
}

runme
```
details:::

### arzhang

loop frequency (Hz): metadata:::get:::arzhang1_object:::loop_frequency

object:::get:::arzhang1_object

### arzhang2

loop frequency (Hz): metadata:::get:::arzhang2_object:::loop_frequency

object:::get:::arzhang2_object

### arzhang3

loop frequency (Hz): metadata:::get:::arzhang3_object:::loop_frequency

object:::get:::arzhang3_object

---

| arzhang | arzhang2 |
|-|-|
| assets:::get:::arzhang1_object/bps.png | assets:::get:::arzhang2_object/bps.png | assets:::get:::arzhang3_object/bps.png |
| assets:::get:::arzhang1_object/ultrasonic-sensor-state.png | assets:::get:::arzhang2_object/ultrasonic-sensor-state.png |
| assets:::get:::arzhang1_object/ultrasonic-sensor-distance-mm.png | assets:::get:::arzhang2_object/ultrasonic-sensor-distance-mm.png |

## observations

- one of the back wheels on arzhang broke. -> 📜
- the on/off switch on arzhang broke -> 📜
- the two arzhangs did not receive each other's advertisements. they both received advertisements from arzhang3. ⚠️ - will review in the next validation.

---

items:::
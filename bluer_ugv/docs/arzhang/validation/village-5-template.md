title:::

UGV(s): ugv_name:::

## script

```bash
runme() {
    @select $1

    @upload public,zip

    @assets publish extensions=gif,push

    # ---

    @select $2

    @swallow ultrasonic review \
    	upload .    

    @assets publish extensions=gif+png,push
}
```

## objects

### arzhang

```bash
runme \
    swallow-debug-2025-10-10-08-49-45-yk18ei \
    2025-10-10-08-52-35-6jjnzn
```

set:::arzhang1_debug_object swallow-debug-2025-10-10-08-49-45-yk18ei
set:::arzhang1_object 2025-10-10-08-52-35-6jjnzn

### arzhang2

```bash
runme \
    swallow-debug-2025-10-10-08-40-38-k8oc2p \
    2025-10-10-08-42-42-ee6oln
```    

set:::arzhang2_debug_object swallow-debug-2025-10-10-08-40-38-k8oc2p
set:::arzhang2_object 2025-10-10-08-42-42-ee6oln

| | [arzhang](../../UGVs/arzhang.md) | [arzhang2](../../UGVs/arzhang2.md) |
|-|-|-|
| loop frequency (Hz) | metadata:::get:::arzhang1_object:::loop_frequency | metadata:::get:::arzhang2_object:::loop_frequency |
| | assets:::get:::arzhang1_object/ultrasonic-sensor-detections.gif | assets:::get:::arzhang2_object/ultrasonic-sensor-detections.gif |
| | assets:::get:::arzhang1_object/ultrasonic-sensor-distance-mm.png | assets:::get:::arzhang2_object/ultrasonic-sensor-distance-mm.png |
| | assets:::get:::arzhang1_debug_object/get:::arzhang1_debug_object.gif | assets:::get:::arzhang2_debug_object/get:::arzhang2_debug_object.gif |

## observations

- ultrasonic sensor is activated when the surface is uneven - will adjust the sensor.
- yolo may not have time to perform the action. -> 📜
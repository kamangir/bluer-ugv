# validations: village-5

UGV(s): 🐬 [`arzhang`](../../UGVs/arzhang.md), 🐬 [`arzhang2`](../../UGVs/arzhang2.md)

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


loop frequency (Hz): 310.87

### arzhang2

```bash
runme \
    swallow-debug-2025-10-10-08-40-38-k8oc2p \
    2025-10-10-08-42-42-ee6oln
```    


loop frequency (Hz): 408.95

---

| [arzhang](../../UGVs/arzhang.md) | [arzhang2](../../UGVs/arzhang2.md) |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-10-10-08-52-35-6jjnzn/ultrasonic-sensor-detections.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-10-10-08-42-42-ee6oln/ultrasonic-sensor-detections.gif?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/2025-10-10-08-52-35-6jjnzn/ultrasonic-sensor-state.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-10-10-08-42-42-ee6oln/ultrasonic-sensor-state.png?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/2025-10-10-08-52-35-6jjnzn/ultrasonic-sensor-distance-mm.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-10-10-08-42-42-ee6oln/ultrasonic-sensor-distance-mm.png?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/swallow-debug-2025-10-10-08-49-45-yk18ei/swallow-debug-2025-10-10-08-49-45-yk18ei.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/swallow-debug-2025-10-10-08-40-38-k8oc2p/swallow-debug-2025-10-10-08-40-38-k8oc2p.gif?raw=true) |

## observations

- ultrasonic sensor is activated when the surface is uneven - will adjust the sensor.
- yolo may not have time to perform the action. -> 📜

---

|   |   |   |
| --- | --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/arzhang/20251010_085451.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/arzhang/20251010_085451.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/arzhang/20251010_085508.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/arzhang/20251010_085508.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/arzhang/20251010_090203.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/arzhang/20251010_090203.jpg?raw=true) |

# bluer-swallow: digital: design: terraform

## Raspbian 64-bit

> ⭐️ preferred.

> ⚠️ on 32-bit, opencv, torch, and other modules install with challenges, and likely at lower versions.

1. follow [RPi](https://github.com/kamangir/bluer-ai/blob/main/bluer_ai/docs/install/RPi.md) (use 64-bit + headless).

2. run in another terminal and paste the seed 🌱 into the ssh window.
```bash
@seed swallow_raspbian clipboard
```

3. run, 
```bash
@swallow env cp driving
```

4. watch for any errors, if none found run,
```bash
@init; @select; @session start
```
now press `t`, wait for ~20 seconds and press `i`. an dataset should be uploaded that contains a few frames from the camera.

![image](https://github.com/kamangir/assets/blob/main/bluer-ugv/terraform-validation.png?raw=true)

the terraform is complete, shut down the machine,
```bash
@host shutdown
```

<details>
<summary>Ubuntu 64-bit</summary>

## Ubuntu 64-bit

> ⚠️ camera needs work.

1. follow [RPi-ROS](https://github.com/kamangir/bluer-ai/blob/main/bluer_ai/docs/install/RPi-ROS.md).

2. run,
```bash
@env dot cp swallow driving
```
</details>

|   |   |   |
| --- | --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/bluer-swallow/20250611_100917.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-swallow/20250611_100917.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bluer-swallow/lab.png?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-swallow/lab.png?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/bluer-swallow/lab2.png?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-swallow/lab2.png?raw=true) |

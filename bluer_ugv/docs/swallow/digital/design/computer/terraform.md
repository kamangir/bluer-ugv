# swallow: digital: design: computer: terraform

## Raspbian 64-bit

1. follow [RPi](https://github.com/kamangir/bluer-ai/blob/main/bluer_ai/docs/install/RPi.md) (use 64-bit + headless or not).

2. run in another terminal and paste the seed 🌱 into the ssh window.
```bash
@seed swallow_raspbian clipboard
```

3. run,
```bash
@bps install
```

4. run, 
```bash
@swallow env cp navigation
@swallow env set full_keyboard 1
@select; @session start
```
now press `t`, then `w`, and wait for ~20 seconds (or press `a`, `d`), then press `zi`. an dataset should be uploaded that contains a few frames from the camera.

![image](https://github.com/kamangir/assets/blob/main/bluer-ugv/terraform-validation.png?raw=true)

5. the terraform is complete, shut down the machine,
```bash
@host shutdown
```


> ⚠️ on 32-bit, opencv, torch, and other modules install with challenges, and likely at lower versions.


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

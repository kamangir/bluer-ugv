# bluer-swallow: digital: design: ultrasonic-sensor: dev

using [ultrasonic_sensor-v8.py](../../../../../../sandbox/ultrasonic_sensor-v8.py).

```text
🐬  left: no detection  | pulse= 11.33 ms | dist≈ 1943 mm
🐬  left: no detection  | pulse= 11.37 ms | dist≈ 1949 mm
🐬  left: detection  | pulse=  0.93 ms | dist≈  159 mm
🐬  left: detection  | pulse=  0.98 ms | dist≈  168 mm
```

using [ultrasonic_sensor-v9.py](../../../../../../sandbox/ultrasonic_sensor-v9.py).

```text
🐬  left    : no detection    ,  11.31 ms ==  1939 mm | right   : no detection    ,  11.32 ms ==  1941 mm
🐬  left    : no detection    ,   5.27 ms ==   904 mm | right   : no detection    ,  11.28 ms ==  1935 mm
🐬  left    : detection       ,   4.50 ms ==   772 mm | right   : no detection    ,   4.75 ms ==   814 mm
🐬  left    : detection       ,   4.34 ms ==   745 mm | right   : detection       ,   4.63 ms ==   795 mm
```

```bash
@select ultrasonic-test-$(@timestamp)
@swallow ultrasonic test - .

@assets publish \
	download,extensions=png,push .
```


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/ultrasonic-test-2025-09-30-12-11-56-5awwdm/pulse--ms-.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/ultrasonic-test-2025-09-30-12-11-56-5awwdm/distance-mm-.png?raw=true) |

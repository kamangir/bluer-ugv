title:::

## test

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
@rpi
@select ultrasonic-test-$(@timestamp)

@swallow ultrasonic test - .
@.

@mac
@select $BLUER_UGV_ULTRASONIC_SENSOR_TEST_OBJECT

@assets publish \
	extensions=png,push

@upload public,zip
@.
```

set:::object_name env:::BLUER_UGV_ULTRASONIC_SENSOR_TEST_OBJECT

| | |
|-|-|
| assets:::get:::object_name/pulse--ms-.png | assets:::get:::object_name/distance-mm-.png |

object:::get:::object_name

## review

```bash
@select $BLUER_UGV_ULTRASONIC_SENSOR_TEST_OBJECT

@swallow ultrasonic review download . \
	--gif 1

@assets publish \
	extensions=gif,push

@upload public,zip
```

set:::object_name env:::BLUER_UGV_ULTRASONIC_SENSOR_TEST_OBJECT

assets:::get:::object_name/ultrasonic-sensor-detections.gif

object:::get:::object_name

## in session

items:::
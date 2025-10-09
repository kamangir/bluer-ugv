title:::

UGV: ugv_name:::

## single thread

```text
::  in 1 min called 8 function(s):
::  #   0 - ClassicalUltrasonicSensor: called 388 time(s), total 46 s, avg 120 ms
::  #   1 - ClassicalYoloCamera: called 388 time(s), total 29 s, avg 076 ms
::  #   2 - ClassicalKeyboard: called 388 time(s), total 489 ms, avg 001 ms
::  #   3 - ClassicalLeds: called 388 time(s), total 081 ms, avg < 1 ms
::  #   4 - ClassicalRightMotor: called 388 time(s), total 072 ms, avg < 1 ms
::  #   5 - ClassicalLeftMotor: called 388 time(s), total 060 ms, avg < 1 ms
::  #   6 - ClassicalPushButton: called 388 time(s), total 025 ms, avg < 1 ms
::  #   7 - ClassicalSetPoint: called 388 time(s), total 005 ms, avg < 1 ms
```

set:::object_name 2025-10-02-18-34-41-g7zbqi

loop frequency (Hz): 7

details:::yaml
metadata:::get:::object_name:::timing
details:::

## multi-threaded

yolo and ultrasonic run on individual threads.

```text
::  in 5 min called 8 function(s):
::  #   0 - session.update: called 5,881 time(s), total 10 s, avg 002 ms
::  #   1 - ClassicalKeyboard: called 5,881 time(s), total 5 s, avg 001 ms
::  #   2 - ClassicalRightMotor: called 5,881 time(s), total 1 s, avg < 1 ms
::  #   3 - ClassicalLeds: called 5,881 time(s), total 1 s, avg < 1 ms
::  #   4 - ClassicalLeftMotor: called 5,881 time(s), total 888 ms, avg < 1 ms
::  #   5 - ClassicalPushButton: called 5,881 time(s), total 417 ms, avg < 1 ms
::  #   6 - ClassicalSetPoint: called 5,881 time(s), total 061 ms, avg < 1 ms
::  #   7 - ClassicalYoloCamera: called 5,881 time(s), total 033 ms, avg < 1 ms
```

set:::object_name 2025-10-09-17-29-38-2d897k

loop frequency (Hz): metadata:::get:::object_name:::loop_frequency

details:::yaml
metadata:::get:::object_name:::timing Hz
details:::

set:::object_gif_name swallow-debug-2025-10-09-17-04-47-vm23uf

assets:::get:::object_gif_name/get:::object_gif_name.gif
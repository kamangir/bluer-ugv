# validations: timing-review

UGV(s): 🐬 [`arzhang2`](../UGVs/arzhang2.md)

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


loop frequency (Hz): 7


<details>
<summary>yaml</summary>

```yaml
ClassicalKeyboard:
  average: 0.0012590726881466928
  count: 388
  total: 0.4885202030009168
ClassicalLeds:
  average: 0.00020801985309429997
  count: 388
  total: 0.08071170300058839
ClassicalLeftMotor:
  average: 0.0001556224587559263
  count: 388
  total: 0.06038151399729941
ClassicalPushButton:
  average: 6.528609278352774e-05
  count: 388
  total: 0.02533100400000876
ClassicalRightMotor:
  average: 0.00018496146648039563
  count: 388
  total: 0.07176504899439351
ClassicalSetPoint:
  average: 1.3237850508823012e-05
  count: 388
  total: 0.005136285997423329
ClassicalUltrasonicSensor:
  average: 0.12047331612371254
  count: 388
  total: 46.743646656000465
ClassicalYoloCamera:
  average: 0.07628990444845254
  count: 388
  total: 29.600482925999586

```

</details>


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


loop frequency (Hz): 570.76


<details>
<summary>yaml</summary>

```yaml
ClassicalKeyboard:
  average: 0.000980741563002365
  count: 5881
  total: 5.7677411320169085
ClassicalLeds:
  average: 0.00019095355415421297
  count: 5881
  total: 1.1229978519809265
ClassicalLeftMotor:
  average: 0.00015103849719449376
  count: 5881
  total: 0.8882574020008178
ClassicalPushButton:
  average: 7.08729685428869e-05
  count: 5881
  total: 0.41680392800071786
ClassicalRightMotor:
  average: 0.0002535338092136507
  count: 5881
  total: 1.4910323319854797
ClassicalSetPoint:
  average: 1.0343385477002432e-05
  count: 5881
  total: 0.060829449990251305
ClassicalYoloCamera:
  average: 5.568318821771838e-06
  count: 5881
  total: 0.032747282990840176
session.update:
  average: 0.0017520639202520283
  count: 5881
  total: 10.303887915002178

```

</details>



![image](https://github.com/kamangir/assets/blob/main/swallow-debug-2025-10-09-17-04-47-vm23uf/swallow-debug-2025-10-09-17-04-47-vm23uf.gif?raw=true)

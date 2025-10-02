# bluer-sparrow: validation: timing-review

UGV: `sparrow2`

## all in the loop

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


loop frequency: `7 Hz`

## ultrasonic thread

```text
::  in 1 min called 7 function(s):
::  #   0 - ClassicalYoloCamera: called 1,344 time(s), total 24 s, avg 019 ms
::  #   1 - ClassicalKeyboard: called 1,344 time(s), total 1 s, avg 001 ms
::  #   2 - ClassicalLeds: called 1,344 time(s), total 245 ms, avg < 1 ms
::  #   3 - ClassicalLeftMotor: called 1,344 time(s), total 164 ms, avg < 1 ms
::  #   4 - ClassicalRightMotor: called 1,344 time(s), total 147 ms, avg < 1 ms
::  #   5 - ClassicalPushButton: called 1,344 time(s), total 073 ms, avg < 1 ms
::  #   6 - ClassicalSetPoint: called 1,344 time(s), total 013 ms, avg < 1 ms
```



<details>
<summary>yaml</summary>

```yaml
ClassicalKeyboard:
  average: 0.0009507089084871993
  count: 1344
  total: 1.277752773006796
ClassicalLeds:
  average: 0.0001820898891353517
  count: 1344
  total: 0.24472881099791266
ClassicalLeftMotor:
  average: 0.00012170681474036169
  count: 1344
  total: 0.1635739590110461
ClassicalPushButton:
  average: 5.456416964410069e-05
  count: 1344
  total: 0.07333424400167132
ClassicalRightMotor:
  average: 0.0001097103534243886
  count: 1344
  total: 0.14745071500237827
ClassicalSetPoint:
  average: 1.00393355695127e-05
  count: 1344
  total: 0.013492867005425069
ClassicalYoloCamera:
  average: 0.018561753730656688
  count: 1344
  total: 24.94699701400259

```

</details>


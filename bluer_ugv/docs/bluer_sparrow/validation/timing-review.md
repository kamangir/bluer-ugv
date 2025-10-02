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


loop frequency: 7 Hz

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


loop frequency: 45.50045661601763


<details>
<summary>yaml</summary>

```yaml
ClassicalKeyboard:
  average: 0.0010086867588569087
  count: 875
  total: 0.882600913999795
ClassicalLeds:
  average: 0.0001818800285810929
  count: 875
  total: 0.1591450250084563
ClassicalLeftMotor:
  average: 5.4980485710465085e-05
  count: 875
  total: 0.04810792499665695
ClassicalPushButton:
  average: 5.346943884796929e-05
  count: 875
  total: 0.046785758991973125
ClassicalRightMotor:
  average: 8.680194971696307e-05
  count: 875
  total: 0.07595170600234269
ClassicalSetPoint:
  average: 1.0828638865599974e-05
  count: 875
  total: 0.009475059007399977
ClassicalYoloCamera:
  average: 0.02050823117143279
  count: 875
  total: 17.944702275003692
session.update:
  average: 0.021977801419425045
  count: 875
  total: 19.230576241996914

```

</details>


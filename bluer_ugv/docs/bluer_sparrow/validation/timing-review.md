# bluer-sparrow: validation: timing-review

UGV: `sparrow2`

```text
::  took 50 s for 8 function call(s):
::  #   0 - ClassicalUltrasonicSensor: called 237 time(s), total 28 s, avg 121 ms
::  #   1 - ClassicalKeyboard: called 237 time(s), total 429 ms, avg 002 ms
::  #   2 - ClassicalLeds: called 237 time(s), total 061 ms, avg < 1 ms
::  #   3 - ClassicalPushButton: called 237 time(s), total 018 ms, avg < 1 ms
::  #   4 - ClassicalRightMotor: called 237 time(s), total 012 ms, avg < 1 ms
```



<details>
<summary>yaml</summary>

```yaml
ClassicalKeyboard:
  count: 79
  total: 0.26060522400121044
ClassicalLeds:
  count: 79
  total: 0.018996546999460406
ClassicalLeftMotor:
  count: 79
  total: 0.0021381899998687004
ClassicalPushButton:
  count: 79
  total: 0.005884663001324952
ClassicalRightMotor:
  count: 79
  total: 0.003850979000389998
ClassicalSetPoint:
  count: 79
  total: 0.001273975000003702
ClassicalUltrasonicSensor:
  count: 79
  total: 9.526912757000673
ClassicalYoloCamera:
  count: 79
  total: 0.0025396730004558776

```

</details>


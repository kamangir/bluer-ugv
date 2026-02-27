# ROS: validations: arzhang4: motor-driver

- uses [swallow/digital/design/rpi-pinout](../../../swallow/digital/design/rpi-pinout.md)
- uses [classical/motor/left](../../../../swallow/session/classical/motor/left.py)
- uses [classical/motor/right](../../../../swallow/session/classical/motor/right.py)

on mac,

```bash
@ROS package create arzhang4
# modifications
```

on rpi, inside the ROS container,

```bash
@ROS package build arzhang4

@ROS test gpio

ros2 run arzhang4 motor_driver
```

```text
[INFO] [1771788343.660588489] [arzhang4_motor_driver]: Motor driver up (RPi.GPIO). BCM pins L(19,13) R(12,18), pwm_hz=800.0, timeout_s=0.35
```

---

# terminology

- `topic`: a continuous stream (cmd_vel, sensor data)
- `service` quick request/response (calibrate, reset)
- `action`: long-running task with feedback (navigate to goal)

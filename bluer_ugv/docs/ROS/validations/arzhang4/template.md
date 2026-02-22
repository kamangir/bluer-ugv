title:::

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
```

🎰

```bash
@ROS test gpio
```

🔥

```bash
ros2 run arzhang4 motor_driver
```

🔥

---

# terminology

- `topic`: a continuous stream (cmd_vel, sensor data)
- `service` quick request/response (calibrate, reset)
- `action`: long-running task with feedback (navigate to goal)

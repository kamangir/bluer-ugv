title:::

- uses [swallow/digital/design/rpi-pinout](../../../swallow/digital/design/rpi-pinout.md)
- uses [classical/motor/left](../../../../swallow/session/classical/motor/left.py)
- uses [classical/motor/right](../../../../swallow/session/classical/motor/right.py)

```bash
@ROS create_package arzhang4
```

🔥

---

# terminology

- `topic`: a continuous stream (cmd_vel, sensor data)
- `service` quick request/response (calibrate, reset)
- `action`: long-running task with feedback (navigate to goal)

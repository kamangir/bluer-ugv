# ROS: validations: gazebo: arzhang4

- uses [arzhang/design/mechanical](../../../arzhang/design/mechanical)
- uses [bluer-sbc/parts/wheel.md](https://github.com/kamangir/bluer-sbc/blob/main/bluer_sbc/docs/parts/wheel.md)

on separate terminals on a mac,

```bash
@ROS gazebo gui serve
```

```bash
@ROS gazebo gui open
```

on a terminal in the ROS container on the same mac,

```bash
@ROS gazebo robot publish
```

on a terminal on the same mac,

```bash
@ROS gazebo robot spawn
```

🔥

```bash
@ROS gazebo robot control linear=2.4,angular=10
```

```bash
gz topic -t /cmd_vel -m gz.msgs.Twist -p "linear: {x: 2.4} angular: {z: 10.0}"
```

|   |
| --- |
| [![image](https://github.com/kamangir/assets3/raw/main/ROS/arzhang4.gif?raw=true)](https://github.com/kamangir/assets3/raw/main/ROS/arzhang4.gif?raw=true) |



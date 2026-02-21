title:::

on separate terminals on a mac,

```bash
@ROS gazebo gui serve
```

```bash
@ROS gazebo gui open
```

on a terminal on the same mac,

```bash
@ROS gazebo publish_robot_description
```

on a terminal on the same mac,


```bash
@ROS gazebo spawn
```

```bash
gz topic -t /cmd_vel -m gz.msgs.Twist -p "linear: {x: 2.4} angular: {z: 10.0}"
```

items:::



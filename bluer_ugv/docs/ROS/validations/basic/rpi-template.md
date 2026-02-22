title:::

```bash
@ROS start
@ROS open
```
```bash
@ROS test ~doctor,gazebo,role=talker
```

```text
⚙️ ros2 topic list
/chatter
/parameter_events
/rosout
ROS_DISTRO: jazzy
ros2: /opt/ros/jazzy/bin/ros2
env vars:
ROS_VERSION=2
ROS_PYTHON_VERSION=3
AMENT_PREFIX_PATH=/opt/ros/jazzy
ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET
ROS_DISTRO=jazzy
packages:
demo_nodes_cpp
demo_nodes_py
role: talker
⚙️ ros2 run demo_nodes_cpp talker
[INFO] [1771593083.707195990] [talker]: Publishing: 'Hello World: 1'
[INFO] [1771593084.707187141] [talker]: Publishing: 'Hello World: 2'
[INFO] [1771593085.707189126] [talker]: Publishing: 'Hello World: 3'
[INFO] [1771593086.707198777] [talker]: Publishing: 'Hello World: 4'
^C[INFO] [1771593086.778762769] [rclcpp]: signal_handler(SIGINT/SIGTERM)
```

in another terminal,

```bash
@ROS open
```
```bash
@ROS test ~doctor,gazebo,role=listener
```

```text
⚙️ ros2 topic list
/parameter_events
/rosout
ROS_DISTRO: jazzy
ros2: /opt/ros/jazzy/bin/ros2
env vars:
ROS_VERSION=2
ROS_PYTHON_VERSION=3
AMENT_PREFIX_PATH=/opt/ros/jazzy
ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET
BLUER_UGV_BEAST_MODEL=UGV-Beast-PI-ROS2-Waveshare
ROS_DISTRO=jazzy
packages:
demo_nodes_cpp
demo_nodes_py
role: listener
⚙️ ros2 run demo_nodes_cpp listener
[INFO] [1771593083.707513508] [listener]: I heard: [Hello World: 1]
[INFO] [1771593084.707440493] [listener]: I heard: [Hello World: 2]
[INFO] [1771593085.707459663] [listener]: I heard: [Hello World: 3]
^C[INFO] [1771593086.060799737] [rclcpp]: signal_handler(SIGINT/SIGTERM)
```



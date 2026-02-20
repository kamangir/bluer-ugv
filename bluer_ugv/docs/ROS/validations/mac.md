# ROS: validations: mac

```bash
@ROS start
@ROS open
```
```bash
@ROS test talker
```

```test
⚙️ ros2 doctor
All 5 checks passed
⚙️ ros2 topic list
/parameter_events
/rosout
ROS_DISTRO: jazzy
ros2: /opt/ros/jazzy/bin/ros2
env vars:
ROS_VERSION=2
ROS_PYTHON_VERSION=3
ROS_DOMAIN_ID=0
AMENT_PREFIX_PATH=/opt/ros/jazzy
ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET
ROS_DISTRO=jazzy
packages:
demo_nodes_cpp
demo_nodes_py
role: talker
⚙️ ros2 run demo_nodes_cpp talker
[INFO] [1771591374.688857335] [talker]: Publishing: 'Hello World: 1'
[INFO] [1771591375.693090419] [talker]: Publishing: 'Hello World: 2'
[INFO] [1771591376.692410628] [talker]: Publishing: 'Hello World: 3'
^C[INFO] [1771591377.628035962] [rclcpp]: signal_handler(SIGINT/SIGTERM)
```

in another terminal,

```bash
@ROS open
```
```bash
@ROS test listener
```

```text
All 5 checks passed
⚙️ ros2 topic list
/parameter_events
/rosout
ROS_DISTRO: jazzy
ros2: /opt/ros/jazzy/bin/ros2
env vars:
ROS_VERSION=2
ROS_PYTHON_VERSION=3
ROS_DOMAIN_ID=0
AMENT_PREFIX_PATH=/opt/ros/jazzy
ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET
BLUER_UGV_BEAST_MODEL=UGV-Beast-PI-ROS2-Waveshare
ROS_DISTRO=jazzy
packages:
demo_nodes_cpp
demo_nodes_py
role: listener
⚙️ ros2 run demo_nodes_cpp listener
[INFO] [1771591374.689461169] [listener]: I heard: [Hello World: 1]
[INFO] [1771591375.693666919] [listener]: I heard: [Hello World: 2]
[INFO] [1771591376.692738086] [listener]: I heard: [Hello World: 3]
^C[INFO] [1771591378.245522920] [rclcpp]: signal_handler(SIGINT/SIGTERM)
```



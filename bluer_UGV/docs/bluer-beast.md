# Blue Beast

based on [UGV Beast PI ROS2](https://www.waveshare.com/ugv-beast-ros2-kit.htm) [order link].

## Battery installation:

> ... 3 x 18650 lithium batteries with a capacity of 2200mA or above ~~and a discharge rate of 4C~~ (vape stores have them)

- instructions: https://www.youtube.com/watch?v=t3EXdMzEUrA

## WiFi

Two modes:

1. AP (Access Point): provides a hotspot: `AccessPopup`, password: `1234567890`
2. STA (Station Mode): connects to a WiFi network.

## Software

1. Controller: `http://<ip-address>:5000/` ("main program")
2. Jupyter Lab: `http://<ip-address>:8888/`
3. ROS

Disable the controller for ROS or some notebook access: https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2_1._Preparation#1.2_Disable_the_main_program_from_running_automatically

## SSH 🔥

```bash
ssh root@<ip-address> -p 23
```

password: `ws`

🔥 achieve with iTerm what is done with MobaXterm: 
1. https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2_1._Preparation#1.4_Remote_login_to_Docker_container
2. https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2_2._RViz_View_Product_Model#2.2_Run_ROS2_robot_driver_node

## ROS 🔥

https://www.xquartz.org/

🔥

- https://www.waveshare.com/wiki/UGV_Beast_PI_ROS2 🔥
- https://github.com/waveshareteam/ugv_rpi

![image](https://github.com/waveshareteam/ugv_rpi/raw/main/media/UGV-Rover-details-23.jpg)

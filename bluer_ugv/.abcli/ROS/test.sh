#! /usr/bin/env bash

function bluer_ugv_ROS_test() {
    local options=$1

    source /opt/ros/jazzy/setup.bash
    ros2 doctor
    ros2 topic list
}

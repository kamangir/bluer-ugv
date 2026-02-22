#! /usr/bin/env bash

function bluer_ugv_ROS_package_create() {
    if [[ "$abcli_is_docker" == false ]]; then
        bluer_ai_log_error "run this command inside the ROS docker container."
        return 1
    fi

    local package_name=${1:-void}

    local options=$2

    bluer_ai_eval path=$(python3 -m bluer_ugv locate)/assets/,$options \
        ros2 pkg create $package_name \
        --build-type ament_python \
        --dependencies rclpy geometry_msgs
}

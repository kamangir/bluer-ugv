#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_publish_robot_description() {
    local options=$1

    if [[ "$abcli_is_docker" == false ]]; then
        bluer_ai_log_error "run this command inside the ROS docker container."
        return 1
    fi

    bluer_ai_badge - "gazebo/robot-description 🦾"

    xacro /root/git/bluer-ugv/bluer_ugv/assets/arzhang4_description/urdf/arzhang4.urdf.xacro >/tmp/arzhang4.urdf

    ros2 run robot_state_publisher robot_state_publisher \
        --ros-args -p robot_description:="$(cat /tmp/arzhang4.urdf)"

    bluer_ai_badge reset
}

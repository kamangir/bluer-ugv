#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_publish_robot_description() {
    local options=$1

    if [[ "$abcli_is_docker" == false ]]; then
        bluer_ai_log_error "run this command inside the ROS docker container."
        return 1
    fi

    bluer_ugv_ROS_gazebo_log

    bluer_ai_badge - "gazebo/robot-description 🦾"

    local path=$(python3 -m bluer_ugv locate)/assets/${GZ_PARTITION}_description/urdf/

    xacro $path/$GZ_PARTITION.urdf.xacro >$path/$GZ_PARTITION.urdf

    ros2 run robot_state_publisher robot_state_publisher \
        --ros-args -p robot_description:="$(cat $path/$GZ_PARTITION.urdf)"

    bluer_ai_badge reset
}

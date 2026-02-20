#! /usr/bin/env bash

function bluer_ugv_ROS_test() {
    local options=$1

    bluer_ai_eval ,$options \
        ros2 doctor
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval ,$options \
        ros2 topic list
    [[ $? -ne 0 ]] && return 1

    bluer_ai_log "ROS_DISTRO: $ROS_DISTRO"
    bluer_ai_log "ros2: $(which ros2)"

    printenv | grep -E 'AMENT|COLCON|RMW|ROS'
}

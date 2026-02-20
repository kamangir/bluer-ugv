#! /usr/bin/env bash

function bluer_ugv_ROS_test() {
    local options=$1
    local role=$(bluer_ai_option_choice "$options" talker,listener talker)

    bluer_ai_eval ,$options \
        ros2 doctor
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval ,$options \
        ros2 topic list
    [[ $? -ne 0 ]] && return 1

    bluer_ai_log "ROS_DISTRO: $ROS_DISTRO"
    bluer_ai_log "ros2: $(which ros2)"

    bluer_ai_log "env vars:"
    printenv | grep -E 'AMENT|COLCON|RMW|ROS'

    bluer_ai_log "packages:"
    ros2 pkg list | grep demo_nodes

    bluer_ai_log "role: $role"
    bluer_ai_eval ,$options \
        ros2 run demo_nodes_cpp $role
}

#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_robot_control() {
    local options=$1
    local linear=$(bluer_ai_option "$options" linear 0.0)
    local angular=$(bluer_ai_option "$options" angular 0.0)
    local partition=$(bluer_ai_option "$options" partition $BLUER_UGV_ROS_DEFAULT_PARTITION)

    if [[ "$abcli_is_mac" == false ]]; then
        bluer_ai_log_warning "run this command in a mac terminal."
        return 1
    fi

    export GZ_PARTITION=$partition
    bluer_ugv_ROS_gazebo_log

    bluer_ai_log "linear: $linear, angular: $angular"

    gz topic \
        -t /cmd_vel \
        -m gz.msgs.Twist \
        -p "linear: {x: $linear} angular: {z: $angular}"
}

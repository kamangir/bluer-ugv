#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_gui_open() {
    local options=$1

    if [[ "$abcli_is_mac" == false ]]; then
        bluer_ai_log_error "run this command in a mac terminal."
        return 1
    fi

    bluer_ugv_ROS_gazebo_log

    bluer_ai_badge - "gazebo/gui 🦾"

    bluer_ai_eval ,$options \
        gz sim -g -v 4

    bluer_ai_badge reset
}

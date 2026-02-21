#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_gui_serve() {
    local options=$1

    if [[ "$abcli_is_mac" == false ]]; then
        bluer_ai_log_error "run this command in a mac terminal."
        return 1
    fi

    bluer_ugv_ROS_gazebo_log

    bluer_ai_badge - "gazebo/gui/server 🦾"

    bluer_ai_eval ,$options \
        gz sim -s -v 4 empty.sdf

    bluer_ai_badge reset
}

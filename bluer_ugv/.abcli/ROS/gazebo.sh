#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo() {
    local options=$1

    if [[ "$abcli_is_docker" == true ]]; then
        bluer_ai_badge - "🦾 gazebo server"

        bluer_ai_eval ,$options \
            gz sim -s -v 4 empty.sdf

        bluer_ai_badge reset
        return
    fi

    if [[ "$abcli_is_mac" == true ]]; then
        :
        return
    fi

    bluer_ai_log_warning "@ROS: gazebo: only works inside the ROS container and on a mac."
    return 1
}

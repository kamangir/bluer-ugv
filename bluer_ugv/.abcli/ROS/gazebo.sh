#! /usr/bin/env bash

export GZ_IP=127.0.0.1
export GZ_PARTITION=arzhang
export GZ_VERBOSE=4

function bluer_ugv_ROS_gazebo() {
    local options=$1
    local do_server=$(bluer_ai_option_int "$options" serve 0)

    if [[ "$do_server" == 1 ]]; then
        bluer_ai_badge - "gazebo server 🦾"

        bluer_ai_eval ,$options \
            gz sim -s -v 4 empty.sdf

        bluer_ai_badge reset
        return
    fi

    bluer_ai_badge - "gazebo gui 🦾"

    bluer_ai_eval ,$options \
        gz sim -g -v 4

    bluer_ai_badge reset
}

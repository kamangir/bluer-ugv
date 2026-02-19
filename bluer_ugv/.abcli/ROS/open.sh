#! /usr/bin/env bash

function bluer_ugv_ROS_open() {
    local options=$1

    local machine_type=""
    [[ "$abcli_is_mac" == true ]] &&
        machine_type="mac"
    [[ "$abcli_is_rpi" == true ]] &&
        machine_type="rpi"
    if [[ -z "$machine_type" ]]; then
        bluer_ai_log_error "@ROS: start: machine type not found."
        return 1
    fi

    bluer_ai_badge - "🦾"

    local init_file="/root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh"

    bluer_ai_eval \
        ,$options \
        sudo docker exec -it bluer_ugv_ros_$machine_type \
        bash --init-file $init_file

    bluer_ai_badge reset
}

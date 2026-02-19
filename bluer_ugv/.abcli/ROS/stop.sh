#! /usr/bin/env bash

function bluer_ugv_ROS_stop() {
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

    bluer_ai_badge - "⚙️🦾"

    bluer_ai_eval \
        path=$(python3 -m bluer_ugv locate)/assets/ROS/$machine_type,$options \
        sudo docker compose down

    bluer_ai_badge reset

}

#! /usr/bin/env bash

function bluer_ugv_ROS_start() {
    local options=$1
    local do_build=$(bluer_ai_option_int "$options" build 0)
    local use_cache=$(bluer_ai_option_int "$options" cache 1)

    local machine_type=""
    [[ "$abcli_is_mac" == true ]] &&
        machine_type="mac"
    [[ "$abcli_is_rpi" == true ]] &&
        machine_type="rpi"
    if [[ -z "$machine_type" ]]; then
        bluer_ai_log_error "@ROS: start: machine type not found."
        return 1
    fi

    local extra_args=""
    [[ $do_build == 1 ]] &&
        extra_args="$extra_args --build"
    [[ $use_cache == 0 ]] &&
        extra_args="$extra_args --no-cache"

    bluer_ai_badge - "⚙️🦾"

    bluer_ai_eval \
        path=$(python3 -m bluer_ugv locate)/assets/ROS/$machine_type,$options \
        sudo docker compose up -d \
        $extra_args

    bluer_ai_badge reset
}

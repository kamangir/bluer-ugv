#! /usr/bin/env bash

function bluer_ugv_ROS_open() {
    local options=$1
    local verbose=$(bluer_ai_option_int "$options" verbose 0)

    local machine_type=""
    [[ "$abcli_is_mac" == true ]] &&
        machine_type="mac"
    [[ "$abcli_is_rpi" == true ]] &&
        machine_type="rpi"
    if [[ -z "$machine_type" ]]; then
        bluer_ai_log_error "@ROS: open: machine type not found."
        return 1
    fi

    local extra_args=""
    [[ "$verbose" == 1 ]] &&
        extra_args="verbose"

    bluer_ai_badge - "🦾"

    local init_file="/root/git/bluer-ugv/bluer_ugv/assets/ROS/bluer_ai.sh"

    bluer_ai_eval \
        ,$options \
        sudo docker exec -it bluer_ugv_ros_$machine_type \
        bash "--init-file $init_file -- $extra_args"
    local status="$?"

    bluer_ai_badge reset

    [[ "$verbose" == 1 ]] &&
        rm -v $abcli_path_git/verbose

    return $status
}

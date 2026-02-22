#! /usr/bin/env bash

export GZ_VERBOSE=4

[[ "$abcli_is_mac" == true ]] &&
    export GZ_IP=$(ipconfig getifaddr en0)

[[ "$abcli_is_docker" == true ]] &&
    export GZ_RELAY=host.docker.internal

function bluer_ugv_ROS_gazebo() {
    local task=$1

    local function_name=bluer_ugv_ROS_gazebo_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    bluer_ai_log_error "@ROS: gazebo: $task: command not found."
    return 1
}

bluer_ai_source_caller_suffix_path /gazebo

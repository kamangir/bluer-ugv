#! /usr/bin/env bash

function bluer_ugv_ROS_arzhang4_test() {
    local options=$1

    local node_name=$2

    local command=""
    [[ "$node_name" == "motor_driver" ]] &&
        command="ros2 topic echo /cmd_vel"

    if [[ -z "$command" ]]; then
        bluer_ai_log_error "node: $node_name not found."
        return 1
    fi

    bluer_ai_badge - "arzhang4 $node_name 🔍"

    bluer_ai_eval ,$options \
        $command \
        "${@:4}"

    bluer_ai_badge reset
}

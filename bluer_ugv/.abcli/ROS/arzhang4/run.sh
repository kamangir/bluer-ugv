#! /usr/bin/env bash

function bluer_ugv_ROS_arzhang4_run() {
    local options=$1

    local node_name=$2

    local command=""
    [[ "$node_name" == "motor_driver" ]] &&
        command="ros2 run arzhang4 motor_driver --ros-args -p debug:=true -p log_period_s:=0.2"
    [[ "$node_name" == "teleop" ]] &&
        command="ros2 run arzhang4 teleop"

    if [[ -z "$command" ]]; then
        bluer_ai_log_error "node: $node_name not found."
        return 1
    fi

    bluer_ai_badge - "arzhang4 $node_name 🐬"

    bluer_ai_eval ,$options \
        $command \
        "${@:4}"

    bluer_ai_badge reset
}

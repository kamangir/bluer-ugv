#! /usr/bin/env bash

function bluer_ugv_ROS_test() {
    local options=$1
    local do_doctor=$(bluer_ai_option_int "$options" doctor 0)
    local role=$(bluer_ai_option "$options" role)

    bluer_ai_log "@ROS: testing ..."

    if [[ "$abcli_is_docker" == true ]]; then
        if [[ "$do_doctor" == 1 ]]; then
            bluer_ai_eval ,$options \
                ros2 doctor
            [[ $? -ne 0 ]] && return 1
        fi

        bluer_ai_eval ,$options \
            ros2 topic list
        [[ $? -ne 0 ]] && return 1

        bluer_ai_log "ROS_DISTRO: $ROS_DISTRO"
        bluer_ai_log "ros2: $(which ros2)"

        bluer_ai_log "env vars:"
        printenv | grep -E 'AMENT|COLCON|RMW|ROS'

        bluer_ai_log "packages:"
        ros2 pkg list | grep demo_nodes
    fi

    bluer_ai_log "gazebo:"
    [[ "$abcli_is_docker" == true ]] &&
        ros2 pkg list | grep ros_gz
    bluer_ai_log "gz: $(which gz)"
    gz sim --version
    [[ $? -ne 0 ]] && return 1

    if [[ ! -z "$role" ]]; then
        bluer_ai_eval ,$options \
            ros2 run demo_nodes_cpp $role
    fi
}

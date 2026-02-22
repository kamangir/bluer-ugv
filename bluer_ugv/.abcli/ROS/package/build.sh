#! /usr/bin/env bash

function bluer_ugv_ROS_package_build() {
    if [[ "$abcli_is_docker" == false ]]; then
        bluer_ai_log_warning "run this command inside the ROS docker container."
        return 1
    fi

    local package_name=${1:-void}

    local options=$2

    local path=$(python3 -m bluer_ugv locate)/assets/$package_name/

    bluer_ai_eval path=$path,$options \
        colcon build
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval path=$path,$options \
        source install/setup.bash
}

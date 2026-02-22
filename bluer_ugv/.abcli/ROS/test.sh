#! /usr/bin/env bash

function bluer_ugv_ROS_test() {
    local options=$1
    local do_doctor=$(bluer_ai_option_int "$options" doctor 0)
    local role=$(bluer_ai_option "$options" role)
    local test_gazebo=$(bluer_ai_option_int "$options" gazebo 0)
    local test_gpio=$(bluer_ai_option_int "$options" gpio 0)

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

    if [[ "$test_gazebo" == 1 ]]; then
        bluer_ai_log "gazebo:"
        [[ "$abcli_is_docker" == true ]] &&
            ros2 pkg list | grep ros_gz
        bluer_ai_log "gz: $(which gz)"
        gz sim --version
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$test_gpio" == 1 ]]; then
        ls -l /proc/device-tree/model || echo "no /proc/device-tree/model"
        ls -l /sys/firmware/devicetree/base/model || echo "no dt model"
        ls -l /dev/gpiomem || echo "no /dev/gpiomem"
        python3 -c "import RPi.GPIO as GPIO; GPIO.setmode(GPIO.BCM); GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW); print('✅ RPi.GPIO')"
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ ! -z "$role" ]]; then
        bluer_ai_eval ,$options \
            ros2 run demo_nodes_cpp $role
    fi
}

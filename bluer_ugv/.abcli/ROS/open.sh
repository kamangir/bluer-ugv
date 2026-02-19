#! /usr/bin/env bash

function bluer_ugv_ROS_open() {
    local options=$1

    bluer_ai_badge - "🦾"

    local init_file="/root/git/bluer-ugv/bluer_ugv/assets/ROS/rpi/bluer_ai.sh"

    bluer_ai_eval \
        ,$options \
        sudo docker exec -it bluer_ugv_ros_rpi \
        bash --init-file $init_file

    bluer_ai_badge reset
}

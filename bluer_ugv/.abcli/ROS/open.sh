#! /usr/bin/env bash

function bluer_ugv_ROS_open() {
    local options=$1

    bluer_ai_badge - 🦾

    bluer_ai_eval \
        ,$options \
        sudo docker exec -it bluer_ugv_ROS \
        bash --init-file /root/git/bluer-ugv/bluer_ugv/ROS/bluer_ai.sh

    bluer_ai_badge reset
}

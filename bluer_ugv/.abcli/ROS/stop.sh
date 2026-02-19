#! /usr/bin/env bash

function bluer_ugv_ROS_stop() {
    local options=$1

    bluer_ai_eval \
        path=$(python3 -m bluer_ugv locate)/ROS,$options \
        sudo docker compose down
}

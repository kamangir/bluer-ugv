#! /usr/bin/env bash

function bluer_ugv_ROS_start() {
    local options=$1

    bluer_ai_eval ,$options \
        sudo docker run \
        -it \
        --network host \
        --privileged ros:jazzy
}

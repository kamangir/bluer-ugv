#! /usr/bin/env bash

function bluer_ugv_ROS_start() {
    local options=$1
    local do_build=$(bluer_ai_option_int "$options" build 1)
    local use_cache=$(bluer_ai_option_int "$options" cache 1)

    local extra_args=""
    [[ $do_build == 1 ]] &&
        extra_args="$extra_args --build"
    [[ $use_cache == 0 ]] &&
        extra_args="$extra_args --no-cache"

    bluer_ai_eval \
        path=$(python3 -m bluer_ugv locate)/assets/ROS/rpi,$options \
        sudo docker compose up -d \
        $extra_args
}

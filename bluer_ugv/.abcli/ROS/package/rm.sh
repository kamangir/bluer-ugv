#! /usr/bin/env bash

function bluer_ugv_ROS_package_rm() {
    local package_name=${1:-void}

    local options=$2

    bluer_ai_eval path=$(python3 -m bluer_ugv locate)/assets/,$options \
        rm -rfv $package_name
}

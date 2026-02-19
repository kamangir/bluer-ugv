#! /usr/bin/env bash

function bluer_ugv_ROS_install() {
    local options=$1

    if [[ "$abcli_is_rpi" == true ]]; then
        pushd $abcli_path_temp >/dev/null
        curl -sSL https://get.docker.com | sh
        if [[ $? -ne 0 ]]; then
            return 1
            popd >/dev/null
        fi

        sudo usermod -aG docker $USER
        popd >/dev/null
    fi
}

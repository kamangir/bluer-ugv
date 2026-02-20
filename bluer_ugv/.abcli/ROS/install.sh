#! /usr/bin/env bash

function bluer_ugv_ROS_install() {
    local options=$1

    if [[ "$abcli_is_rpi" == true ]]; then
        pushd $abcli_path_temp >/dev/null
        bluer_ai_eval ,$options \
            curl \
            --fail \
            --show-error \
            --location \
            --progress-bar \
            --output get-docker.sh \
            https://get.docker.com
        [[ $? -ne 0 ]] && return 1

        chmod +x get-docker.sh
        sudo ./get-docker.sh
        [[ $? -ne 0 ]] && return 1

        sudo usermod -aG docker $USER
        popd >/dev/null
    fi
}

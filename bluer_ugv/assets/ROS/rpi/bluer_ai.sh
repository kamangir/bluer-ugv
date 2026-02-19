#! /usr/bin/env bash

function bluer_ugv_ROS_container_install() {
    python3 -m venv /root/venv/bluer_ai
    source /root/venv/bluer_ai/bin/activate

    pip install --upgrade pip
    [[ $? -ne 0 ]] && return 1

    pip install blueness
    [[ $? -ne 0 ]] && return 1

    local repo_name
    for repo_name in \
        bluer-options \
        bluer-objects \
        bluer-ai \
        bluer-algo \
        bluer-agent \
        bluer-sbc \
        bluer-ugv; do

        cd /root/git/$repo_name
        pip install -e .
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}

function bluer_ugv_ROS_container_open() {
    local check_filename=/root/git/entry-completed
    if [[ ! -f "$check_filename" ]]; then
        echo "🐬 installing bluer-ugv/ROS container requirements..."

        bluer_ugv_ROS_container_install
        [[ $? -ne 0 ]] && return 1

        touch $check_filename
    fi

    source /root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh
}

bluer_ugv_ROS_container_open

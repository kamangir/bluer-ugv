#! /usr/bin/env bash

function bluer_ugv_ROS_container_install() {
    python3 -m venv /root/venv/bluer_ai
    source /root/venv/bluer_ai/bin/activate

    pip install --upgrade pip

    pip install blueness

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
    done
}

function bluer_ugv_ROS_container_open() {
    local check_filename=/root/git/entry-completed
    if [[ ! -f "$check_filename" ]]; then
        bluer_ugv_ROS_container_install
        touch $check_filename
    fi

    source /root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh
}

bluer_ugv_ROS_container_open

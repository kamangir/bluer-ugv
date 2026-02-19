#! /usr/bin/env bash

function install_bluer_ugv_ROS() {
    sudo apt update
    sudo apt install -y \
        python3-venv \
        python3-pip \
        build-essential &&
        rm -rf /var/lib/apt/lists/*

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

function open_bluer_ugv_ROS() {
    local check_filename=/root/git/entry-completed
    if [[ ! -f "$check_filename" ]]; then
        install_bluer_ugv_ROS
        touch $check_filename
    fi

    source /root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh
}

open_bluer_ugv_ROS

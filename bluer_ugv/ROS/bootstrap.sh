#! /usr/bin/env bash

function runme() {
    if [[ ! -d "/root/venv/bluer_ai" ]]; then
        echo "📜 venv not found, creating..."

        sudo apt update
        sudo apt install -y python3-venv python3-pip

        python3 -m venv /root/venv/bluer_ai

        pip install -U pip setuptools wheel

        pip install blueness
    fi
    source /root/venv/bluer_ai/bin/activate
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
        [[ $? -ne 0 ]] && return 1

        echo "📜 installing $repo_name..."
        pip install -e .
        [[ $? -ne 0 ]] && return 1
    done

    source /root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh
}

runme

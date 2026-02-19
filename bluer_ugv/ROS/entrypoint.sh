#! /usr/bin/env bash

function entrypoint() {
    local check_filename=/root/git/entry-completed
    if [[ -f "$check_filename" ]]; then
        echo "✅ entrypoint."
        return 0
    fi

    pip install --upgrade pip

    python3 -m venv /root/venv/bluer_ai
    source /root/venv/bluer_ai/bin/activate

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

    touch $check_filename
}

entrypoint

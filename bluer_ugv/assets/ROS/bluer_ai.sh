#! /usr/bin/env bash

function bluer_ugv_ROS_container_init() {
    local filename=/root/bluer_ugv_ROS_container_installed
    if [[ -f "$filename" ]]; then
        echo "🐬 @ROS: container ✅"
    else
        echo "🐬 @ROS: installing container dependencies..."

        # ROS environment
        source /opt/ros/jazzy/setup.bash
        [[ $? -ne 0 ]] && return 1

        python3 -m venv /root/venv/bluer_ai
        [[ $? -ne 0 ]] && return 1

        source /root/venv/bluer_ai/bin/activate
        [[ $? -ne 0 ]] && return 1

        pip install --upgrade pip setuptools wheel
        [[ $? -ne 0 ]] && return 1

        local list_of_repos="bluer-options"
        # bluer-objects bluer-ai bluer-algo bluer-agent bluer-sbc bluer-ugv
        for repo in $list_of_repos; do
            if [[ ! -d "/root/git/$repo" ]]; then
                echo "⚠️ /root/git/$repo not found"
                return 1
            fi

            echo "🐬 @ROS: pip installing $repo..."
            pip install -e "/root/git/$repo"
            [[ $? -ne 0 ]] && return 1
        done

        touch $filename
    fi

    source /root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh
}

bluer_ugv_ROS_container_init

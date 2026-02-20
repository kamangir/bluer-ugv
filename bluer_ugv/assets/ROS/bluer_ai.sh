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

        pip install --no-cache-dir blueness
        [[ $? -ne 0 ]] && return 1

        local list_of_repos="bluer-options bluer-objects bluer-ai bluer-algo bluer-agent bluer-sbc bluer-ugv"
        for repo in $list_of_repos; do
            if [[ ! -d "/root/git/$repo" ]]; then
                echo "⚠️ /root/git/$repo not found"
                return 1
            fi

            echo "🐬 @ROS: installing $repo..."
            pip install -e "/root/git/$repo"
            [[ $? -ne 0 ]] && return 1
        done

        apt-get update

        echo "🐬 @ROS: fixing opencv..."
        apt-get install -y --no-install-recommends \
            libgl1 \
            libglib2.0-0t64
        [[ $? -ne 0 ]] && return 1
        python3 -c "import cv2; print('✅ opencv', cv2.__version__)"
        [[ $? -ne 0 ]] && return 1

        echo "🐬 @ROS: getting demos..."
        apt-get install -y \
            ros-jazzy-demo-nodes-cpp \
            ros-jazzy-demo-nodes-py
        [[ $? -ne 0 ]] && return 1

        echo "🐬 @ROS: getting gazebo..."
        sudo apt update
        sudo apt install -y \
            ros-jazzy-ros-gz \
            ros-jazzy-xacro \
            ros-jazzy-robot-state-publisher \
            ros-jazzy-joint-state-publisher \
            ros-jazzy-joint-state-publisher-gui

        touch $filename
    fi

    source /opt/ros/jazzy/setup.bash
    export PATH="/opt/ros/jazzy/opt/gz_tools_vendor/bin:$PATH"

    export BLUER_AI_IGNORED_EXTERNAL_PLUGINS="abadpour,bluer-academy,bluer-flow,bluer-geo,bluer-journal,bluer-plugin,bluer-resistance,bluer-sandbox,bluer-south,btc-prediction-bash,giza"
    source /root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh ~verbose
}

bluer_ugv_ROS_container_init

#! /usr/bin/env bash

function bluer_ugv_ROS_container_init() {
    local machine_type=""
    local machine_type_
    for machine_type_ in mac rpi; do
        if [[ -f /root/storage/temp/ROS-is-on-$machine_type_ ]]; then
            machine_type=$machine_type_
            break
        fi
    done
    if [[ -z "$machine_type" ]]; then
        echo "❗️ machine type not found."
        return 1
    fi
    echo "🐬 @ROS: machine_type: $machine_type"

    local filename=/root/bluer_ugv_ROS_container_installed
    if [[ -f "$filename" ]]; then
        echo "🐬 @ROS: container ✅"
    else
        echo "🐬 @ROS: installing container dependencies..."

        # ROS environment
        source /opt/ros/jazzy/setup.bash
        [[ $? -ne 0 ]] && return 1

        /usr/bin/python3 -m venv --system-site-packages /root/venv/bluer_ai
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

        echo "🐬 @ROS: fixing opencv..."
        apt-get update
        apt-get install -y --no-install-recommends \
            libgl1 \
            libglib2.0-0t64
        [[ $? -ne 0 ]] && return 1

        python3 -c "import cv2; print('✅ opencv', cv2.__version__)"
        [[ $? -ne 0 ]] && return 1

        echo "🐬 @ROS: getting demos..."
        apt-get update
        apt-get install -y \
            ros-jazzy-demo-nodes-cpp \
            ros-jazzy-demo-nodes-py
        [[ $? -ne 0 ]] && return 1

        if [[ "$machine_type" == mac ]]; then
            echo "🐬 @ROS: getting gazebo..."
            sudo apt update
            sudo apt install -y \
                ros-jazzy-ros-gz \
                ros-jazzy-xacro \
                ros-jazzy-robot-state-publisher \
                ros-jazzy-joint-state-publisher \
                ros-jazzy-joint-state-publisher-gui
            [[ $? -ne 0 ]] && return 1
        fi

        if [[ "$machine_type" == rpi ]]; then
            echo "🐬 @ROS: getting gpio..."
            apt update
            apt install -y python3-rpi-lgpio python3-lgpio
            [[ $? -ne 0 ]] && return 1

            python3 -c "import RPi.GPIO as GPIO; print('✅ RPi.GPIO');"
            [[ $? -ne 0 ]] && return 1
        fi

        touch $filename
    fi

    source /opt/ros/jazzy/setup.bash
    export PATH="/opt/ros/jazzy/opt/gz_tools_vendor/bin:$PATH"

    export BLUER_AI_IGNORED_EXTERNAL_PLUGINS="abadpour,bluer-academy,bluer-flow,bluer-geo,bluer-journal,bluer-plugin,bluer-resistance,bluer-sandbox,bluer-south,btc-prediction-bash,giza"
    source /root/git/bluer-ai/bluer_ai/.abcli/bluer_ai.sh ~verbose
}

bluer_ugv_ROS_container_init

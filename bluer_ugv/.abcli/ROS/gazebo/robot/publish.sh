#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_robot_publish() {
    local options=$1

    if [[ "$abcli_is_docker" == false ]]; then
        bluer_ai_log_error "run this command inside the ROS docker container."
        return 1
    fi

    bluer_ugv_ROS_gazebo_log

    bluer_ai_badge - "gazebo/robot 🦾"

    local path=$(python3 -m bluer_ugv locate)/assets/${GZ_PARTITION}_description/urdf/

    xacro $path/$GZ_PARTITION.urdf.xacro >$path/$GZ_PARTITION.urdf
    [[ $? -ne 0 ]] && return 1

    python3 -m bluer_ugv.ROS generate_rsp_yaml \
        --urdf_path $path/$GZ_PARTITION.urdf
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval ,$options \
        ros2 run robot_state_publisher robot_state_publisher \
        --ros-args --params-file "$path/${GZ_PARTITION}_rsp.yaml"
    [[ $? -ne 0 ]] && return 1

    bluer_ai_badge reset
}

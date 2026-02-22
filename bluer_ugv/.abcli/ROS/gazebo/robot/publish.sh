#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_robot_publish() {
    local options=$1
    local partition=$(bluer_ai_option "$options" partition $BLUER_UGV_ROS_DEFAULT_PARTITION)

    if [[ "$abcli_is_docker" == false ]]; then
        bluer_ai_log_error "run this command inside the ROS docker container."
        return 1
    fi

    export GZ_PARTITION=$partition
    bluer_ugv_ROS_gazebo_log

    bluer_ai_badge - "gazebo/robot 🦾"

    local path=$(python3 -m bluer_ugv locate)/assets/${partition}_description/urdf/

    xacro $path/$partition.urdf.xacro >$path/$partition.urdf
    [[ $? -ne 0 ]] && return 1

    python3 -m bluer_ugv.ROS \
        generate_rsp_yaml \
        --urdf_path $path/$partition.urdf
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval ,$options \
        ros2 run robot_state_publisher robot_state_publisher \
        --ros-args --params-file "$path/${partition}_rsp.yaml"
    [[ $? -ne 0 ]] && return 1

    bluer_ai_badge reset
}

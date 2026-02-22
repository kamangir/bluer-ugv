#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_robot_spawn() {
    local options=$1
    local partition=$(bluer_ai_option "$options" partition $BLUER_UGV_ROS_DEFAULT_PARTITION)

    if [[ "$abcli_is_mac" == false ]]; then
        bluer_ai_log_warning "run this command in a mac terminal."
        return 1
    fi

    export GZ_PARTITION=$partition
    bluer_ugv_ROS_log

    local path=$(python3 -m bluer_ugv locate)/assets/${partition}_description/urdf/

    gz sdf -p $path/$partition.urdf >$path/$partition.sdf
    [[ $? -ne 0 ]] && return 1

    gz service -s /world/empty/create \
        --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean \
        --timeout 5000 \
        --req "sdf_filename: '$path/$partition.sdf', name: '$partition', pose: {position: {x: 0, y: 0, z: 0.3}}"
}

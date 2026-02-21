#! /usr/bin/env bash

function bluer_ugv_ROS_gazebo_spawn() {
    local options=$1

    if [[ "$abcli_is_mac" == false ]]; then
        bluer_ai_log_error "run this command in a mac terminal."
        return 1
    fi

    bluer_ugv_ROS_gazebo_log

    local path=$(python3 -m bluer_ugv locate)/assets/${GZ_PARTITION}_description/urdf/

    gz sdf -p $path/$GZ_PARTITION.urdf >$path/$GZ_PARTITION.sdf
    [[ $? -ne 0 ]] && return 1

    head -n 5 $path/$GZ_PARTITION.sdf

    gz service -s /world/empty/create \
        --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean \
        --timeout 5000 \
        --req "sdf_filename: '$path/$GZ_PARTITION.sdf', name: '$GZ_PARTITION', pose: {position: {x: 0, y: 0, z: 0.3}}"
}

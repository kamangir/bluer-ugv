#! /usr/bin/env bash

function bluer_ugv_ROS_arzhang4() {
    local task=$1

    local function_name=bluer_ugv_ROS_arzhang4_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        local options=$2
        local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
        local do_build=$(bluer_ai_option_int "$options" build $(bluer_ai_not $do_dryrun))

        if [[ "$do_build" == 1 ]]; then
            bluer_ugv_ROS_package_build arzhang4
            [[ $? -ne 0 ]] && return 1
        fi

        $function_name "${@:2}"
        return
    fi

    bluer_ai_log_error "@arzhang4: $task: command not found."
    return 1
}

bluer_ai_source_caller_suffix_path /arzhang4

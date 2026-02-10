#! /usr/bin/env bash

function bluer_ugv_swallow_env_set() {
    local keyword=${1:-void}

    local var_name=$(python3 -m bluer_ugv.swallow.env \
        get_var_name \
        --keyword "$keyword")

    if [[ -z "$var_name" ]]; then
        bluer_ai_log_error "$keyword: var not found."
        return 1
    fi

    local value=${2:-1}

    bluer_ai_eval path=$abcli_path_git/bluer-sbc \
        dotenv set \
        $var_name \
        "$value"
    [[ $? -ne 0 ]] && return 1

    bluer_sbc init
}

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

    pushd $abcli_path_git/bluer-sbc >/dev/null

    dotenv set \
        $var_name \
        "${@:2}"
    [[ $? -ne 0 ]] && return 1

    popd >/dev/null

    bluer_sbc init
}

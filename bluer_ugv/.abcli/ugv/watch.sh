#! /usr/bin/env bash

function bluer_ugv_watch() {
    local ugv_name=$1
    local location=$2

    local computer_name=$(bluer_ugv_get "$ugv_name" computers.$location)
    if [[ "$computer_name" == "not-found" ]]; then
        bluer_ai_log_error "$ugv_name.$location not found."
        return 1
    fi

    bluer_ai_log "ssh $ugv_name.$location ($computer_name)..."

    bluer_ai_log watch rpi $computer_name
}

#! /usr/bin/env bash

function bluer_UGV() {
    local task=${1:-version}

    bluer_ai_generic_task \
        plugin=bluer_UGV,task=$task \
        "${@:2}"
}

bluer_ai_log $(bluer_UGV version --show_icon 1)

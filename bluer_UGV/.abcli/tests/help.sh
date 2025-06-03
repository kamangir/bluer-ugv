#! /usr/bin/env bash

function test_bluer_UGV_help() {
    local options=$1

    local module
    for module in \
        "@UGV" \
        \
        "@UGV pypi" \
        "@UGV pypi browse" \
        "@UGV pypi build" \
        "@UGV pypi install" \
        \
        "@UGV pytest" \
        \
        "@UGV test" \
        "@UGV test list" \
        \
        "bluer_UGV"; do
        bluer_ai_eval ,$options \
            bluer_ai_help $module
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done

    return 0
}

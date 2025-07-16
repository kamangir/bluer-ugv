#! /usr/bin/env bash

function bluer_ugv_swallow_env_cp() {
    bluer_ai_env_dot_cp swallow-raspbian-${1:-navigation}
    [[ $? -ne 0 ]] && return 1

    bluer_ugv init clear
}

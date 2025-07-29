#! /usr/bin/env bash

function test_bluer_ugv_parts_adjust() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_ugv parts adjust \
        - \
        --verbose 1
}

#! /usr/bin/env bash

function test_bluer_UGV_version() {
    local options=$1

    bluer_ai_eval ,$options \
        "bluer_UGV version ${@:2}"
}

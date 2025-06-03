#! /usr/bin/env bash

function test_bluer_UGV_README() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_UGV build_README
}

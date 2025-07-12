#! /usr/bin/env bash

function test_bluer_ugv_swallow_dataset_review() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_ugv_swallow_dataset_review \
        ,$options \
        2025-07-09-10-59-15-x9eemj
}

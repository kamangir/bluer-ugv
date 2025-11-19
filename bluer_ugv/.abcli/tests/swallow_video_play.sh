#! /usr/bin/env bash

function swallow_video_play() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        play
}

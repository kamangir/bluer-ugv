#! /usr/bin/env bash

function swallow_video_play_pause_stop() {
    local options=$1

    local do_dryrun=0
    [[ "$abcli_is_rpi" == false ]] &&
        do_dryrun=1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        play \
        download,dryrun=$do_dryrun,video=loading
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        pause \
        dryrun=$do_dryrun
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        stop \
        dryrun=$do_dryrun
}

#! /usr/bin/env bash

function bluer_ugv_swallow_video_pause() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    bluer_ai_eval - \
        python3 -m bluer_ugv.swallow.session.classical.screen.video \
        --pause \
        --dryrun $do_dryrun \
        "${@:2}"
}

#! /usr/bin/env bash

function bluer_ugv_swallow_video_pause() {
    python3 -m bluer_ugv.swallow.session.classical.screen.video \
        --pause \
        "$@"
}

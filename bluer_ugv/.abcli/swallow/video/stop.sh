#! /usr/bin/env bash

function bluer_ugv_swallow_video_stop() {
    python3 -m bluer_ugv.swallow.session.classical.screen.video \
        stop \
        "$@"
}

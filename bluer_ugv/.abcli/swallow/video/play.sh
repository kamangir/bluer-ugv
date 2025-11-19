#! /usr/bin/env bash

function bluer_ugv_swallow_video_play() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local video=$(bluer_ai_option "$options" video loading)

    local object_name=$(bluer_ai_clarify_object $2 $RANGIN_VIDEO_LIST_OBJECT)

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_ugv_swallow.video \
        leaf \
        --object_name $object_name \
        --download $do_download \
        --dryrun $do_dryrun \
        --video $video \
        "${@:3}"
}

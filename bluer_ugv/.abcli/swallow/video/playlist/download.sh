#! /usr/bin/env bash

function bluer_ugv_swallow_video_playlist_download() {
    local options=${1:-policy=doesnt_exist}

    bluer_objects_download \
        filename=metadata.yaml \
        $RANGIN_VIDEO_LIST_OBJECT

    bluer_objects_download \
        ,$options \
        $RANGIN_VIDEO_LIST_OBJECT
}

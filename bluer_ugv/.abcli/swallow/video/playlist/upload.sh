#! /usr/bin/env bash

function bluer_ugv_swallow_video_node_upload() {
    local options=${1:-filename=metadata.yaml}

    bluer_objects_upload \
        ,$options \
        $RANGIN_VIDEO_LIST_OBJECT
}

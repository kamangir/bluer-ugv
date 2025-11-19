#! /usr/bin/env bash

function bluer_ugv_swallow_video_node_edit() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download \
            filename=metadata.yaml \
            $RANGIN_VIDEO_LIST_OBJECT

    bluer_ai_code \
        $ABCLI_OBJECT_ROOT/$RANGIN_VIDEO_LIST_OBJECT/metadata.yaml
}

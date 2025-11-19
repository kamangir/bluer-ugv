#! /usr/bin/env bash

function swallow_video_playlist_cat() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        playlist \
        cat \
        download
}

function swallow_video_playlist_download_upload() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        playlist \
        download \
        policy=doesnt_exist
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        playlist \
        upload \
        filename=metadata.yaml
}

function swallow_video_playlist_edit() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_ugv \
        swallow \
        playlist \
        edit \
        download
}

#! /usr/bin/env bash

function bluer_ugv_rangin_init() {
    local options=$1
    local do_install=$(bluer_ai_option_int "$options" install 0)

    if [[ "$do_install" == 1 ]]; then
        [[ "$abcli_is_rpi" == 1 ]] &&
            sudo apt install -y alsa-utils wlr-randr
    fi

    [[ "$abcli_is_rpi" == 1 ]] &&
        wlr-randr --output HDMI-A-1 --transform 90
}

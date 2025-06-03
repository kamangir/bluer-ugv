#! /usr/bin/env bash

function bluer_UGV_action_git_before_push() {
    bluer_UGV build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(bluer_ai_git get_branch)" != "main" ]] &&
        return 0

    bluer_UGV pypi build
}

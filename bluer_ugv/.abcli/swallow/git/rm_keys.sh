#! /usr/bin/git bash

function bluer_ugv_swallow_git_rm_keys() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    if [[ "$abcli_is_rpi" == false ]]; then
        bluer_ai_log_error "only works on rpi."
        return 1
    fi

    bluer_ai_eval dryrun=$do_dryrun \
        rm -v ~/.ssh/$BLUER_AI_GIT_SSH_KEY_NAME

    bluer_ai_eval dryrun=$do_dryrun \
        rm -v ~/.ssh/$BLUER_AI_GIT_SSH_KEY_NAME.pub

    local repo
    for repo in $(bluer_ai_plugins list_of_external --delim space --log 0 --repo_names 1); do
        bluer_ai_eval dryrun=$do_dryrun \
            bluer_ai_git_set_remote \
            $repo_name \
            dryrun=$do_dryrun,https
        [[ $? -ne 0 ]] && return 1

        git pull
        [[ $? -ne 0 ]] && return 1
    done
}

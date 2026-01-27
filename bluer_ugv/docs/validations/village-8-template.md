title:::

ugv_name:::

validation of connection and code update during offline.

on separate terminals,

```bash
@ugv ssh arzhang2 back

@ugv ssh arzhang2 front

@ugv watch arzhang2 back

@ugv watch arzhang2 front
```

🔥 👦🏽

```bash
runme() {
    local repo_name
    local machine_name
    for repo_name in @ai @objects @options; do
        for machine_name in sparrow2 sparrow3-back; do
            @git $repo_name push update scp,rpi=$machine_name
        done
    done
}

runme
```

🔥
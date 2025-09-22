title:::

items:::

```bash
runme() {
    local list_of_objects

@ls local,objects --prefix swallow-debug-$(@today)
# upload all

@ls cloud,objects --prefix $(@today)
```

}

runme
🔥
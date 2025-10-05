title:::

UGV: [`arzhang2`](../../UGVs/arzhang2.md)

## debug object

```bash
runme() {
    @select $1

    @upload public,zip

    @assets publish extensions=gif,push
}

runme swallow-debug-2025-09-26-17-44-51-6pb87y
```

set:::object1_name swallow-debug-2025-09-26-17-44-51-6pb87y
set:::object2_name swallow-debug-2025-09-27-19-15-31-6iq5vz

## observations

- wheels functioned as expected. ✅
- robot rebooted after a minute of operation and again. ⚠️ loose power connections on shield found and fixed, subsequent testing validated the fix. ✅
- camera is upside down - fixed. ✅

```bash
runme swallow-debug-2025-09-27-19-15-31-6iq5vz
```

| | |
|-|-|
| object:::get:::object1_name | object:::get:::object2_name |
| assets:::get:::object1_name/get:::object1_name.gif | assets:::get:::object2_name/get:::object2_name.gif |

items:::
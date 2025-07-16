title:::

# mac

both on mac.

```bash
@ugv socket test - \
    --what receiving
```

```bash
@ugv socket test - \
    --host dev.local \
    --what sending
```

✅

# rpi -> mac

on mac:

```bash
@ugv socket test - \
    --what receiving
```

on rpi:

```bash
@ugv socket test - \
    --host dev.local \
    --what sending
```

✅

# mac -> rpi

on rpi:

```bash
@ugv socket test - \
    --what receiving
```

on mac:

```bash
@ugv socket test - \
    --host swallow2.local \
    --what sending
```

✅
title:::

```bash
@list log \
    $(@list filter \
        $(@swallow dataset list) \
        --contains $(@today))
```

> list of 3 item(s): 2025-07-13-10-15-29-46j4oy, 2025-07-13-10-37-12-d4iwpm, 2025-07-13-12-55-54-cx5mhk.

---

```bash
runme() {
    local object_name
    for object_name in $(@list filter \
        $(@swallow dataset list) \
        --contains $(@today) | tr , " "); do
        @select $object_name

        @download policy=doesnt_exist .
        @upload public,zip .
        @assets publish \
            extensions=png,push . \
            --prefix grid
    done
}

runme
```

set:::object_name 2025-07-13-10-15-29-46j4oy

object:::get:::object_name

| | |
|-|-|
| assets:::get:::object_name/grid.png | assets:::get:::object_name/grid-timeline.png |

set:::object_name 2025-07-13-10-37-12-d4iwpm

object:::get:::object_name

| | |
|-|-|
| assets:::get:::object_name/grid.png | assets:::get:::object_name/grid-timeline.png |

set:::object_name 2025-07-13-12-55-54-cx5mhk

object:::get:::object_name

| | |
|-|-|
| assets:::get:::object_name/grid.png | assets:::get:::object_name/grid-timeline.png |
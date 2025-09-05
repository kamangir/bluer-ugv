title:::

items:::

```bash
runme() {
    local options=$1
    local do_publish=$(@option::int "$options" publish 1)

    local object_name=$2
    @select $object_name

    @download policy=doesnt_exist

    [[ "$do_publish" == 1 ]] &&
        @upload public,zip
}

runme - 2025-09-05-11-48-27-d56azo
```

set:::object_name 2025-09-05-11-48-27-d56azo

object:::get:::object_name

assets:::get:::object_name/grid.png

assets:::get:::object_name/grid-timeline.png

metadata:::get:::object_name

assets:::get:::object_name/VID-20250905-WA0014_1.gif
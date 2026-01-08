title:::

ugv_name:::

## objects

details:::code
```bash
@ls cloud,objects --prefix 2025-12-09
```
```text
🌀   7 objects(s)
🌀  #   0 - 2025-12-09-08-16-53-a4rfg2
🌀  #   1 - 2025-12-09-08-52-54-jre3xs
🌀  #   2 - 2025-12-09-09-09-43-ljsjbb
🌀  #   3 - 2025-12-09-10-51-24-2dfnau
🌀  #   4 - 2025-12-09-14-36-28-3o4zvv
🌀  #   5 - 2025-12-09-16-42-23-h1awiz
🌀  #   6 - 2025-12-09-18-52-03-7jo931
```

```bash
runme() {
    local options=$1
    local publish=$(@option::int "$options" publish 1)
    local upload=$(@option::int "$options" upload 1)

    local object_name
    for object_name in $(@ls \
        cloud,objects \
        --log 0 \
        --delim space \
        --prefix 2025-12-09); do

        @select $object_name

        @download policy=doesnt_exist    

        [[ "$upload" == 1 ]] &&
            @upload public,zip

        [[ "$publish" == 1 ]] &&
            @assets publish extensions=png,push . \
            --prefix ultrasonic
    done
}

runme ~upload
```

```bash
@select 2025-12-09-18-52-03-7jo931
@gif ~download,~upload . --frame_count=200 --output_filename 200.gif
@upload filename=200.gif
@assets publish extensions=gif,push
```
details:::

objects:::

## debug object

details:::code
```bash
@ls cloud,objects --prefix swallow-debug-2025-12-09
```
```text
🌀   1 objects(s)
🌀  #   0 - swallow-debug-2025-12-09-15-43-31-o6gh5k
```

```bash
runme() {
    local object_name=$(@list resize $(@ls cloud,objects \
    --prefix swallow-debug-2025-12-09 \
    --log 0 \
    --delim ,) \
    1 \
    --delim space)
    @select 
    @assets publish \
        download,extensions=gif,push \
        $object_name
}

runme
```
details:::

set:::object_debug_name swallow-debug-2025-12-09-15-43-31-o6gh5k
set:::object_name 2025-12-09-18-52-03-7jo931

| | |
|-|-|
| assets:::get:::object_debug_name/get:::object_debug_name.gif | assets:::get:::object_name/200.gif |

## observations

1. 1.8 km drive, battery lasted with ~20 minutes of recharge at the middle.
2. ugv steers right when driving forward, likely because of wheel shaft misalignments.

items:::
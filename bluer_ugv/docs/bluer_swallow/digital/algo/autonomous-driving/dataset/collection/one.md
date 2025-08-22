# bluer_swallow: digital: algo: autonomous-driving: dataset: collection: one

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


[2025-07-13-10-15-29-46j4oy](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-07-13-10-15-29-46j4oy.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-15-29-46j4oy/grid.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-15-29-46j4oy/grid-timeline.png?raw=true) |


[2025-07-13-10-37-12-d4iwpm](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-07-13-10-37-12-d4iwpm.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-37-12-d4iwpm/grid.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-37-12-d4iwpm/grid-timeline.png?raw=true) |


[2025-07-13-12-55-54-cx5mhk](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-07-13-12-55-54-cx5mhk.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-12-55-54-cx5mhk/grid.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-12-55-54-cx5mhk/grid-timeline.png?raw=true) |

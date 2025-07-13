# bluer_swallow: digital: dataset: collection: one

```bash
@select $BLUER_UGV_SWALLOW_DATASET_LIST
@list log \
    $(@list filter \
	$(@metadata get \
	key=dataset-list,object .) \
    --contains $(@today))
```

> TBA

---

```bash
runme() {
    local object_name
    for object_name in $(@list filter \
        $(@metadata get \
        key=dataset-list,object \
        $BLUER_UGV_SWALLOW_DATASET_LIST) \
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


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-15-29-46j4oy/grid.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-15-29-46j4oy/grid-timeline.png?raw=true) |


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-37-12-d4iwpm/grid.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-10-37-12-d4iwpm/grid-timeline.png?raw=true) |


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-12-55-54-cx5mhk/grid.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-07-13-12-55-54-cx5mhk/grid-timeline.png?raw=true) |

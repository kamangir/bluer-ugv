# bluer_swallow: digital: dataset: collection: one

metadata:::$BLUER_UGV_SWALLOW_DATASET_LIST

```bash
@select $BLUER_UGV_SWALLOW_DATASET_LIST
@list log \
    $(@list filter \
	$(@metadata get \
	key=dataset-list,object .) \
    --contains $(@today))
```

> list of 7 item(s): 2025-07-13-10-04-43-eij8l0, 2025-07-13-10-15-29-46j4oy, 2025-07-13-10-37-12-d4iwpm, 2025-07-13-12-27-56-q1os6s, 2025-07-13-12-32-18-e9hqed, 2025-07-13-12-37-23-iy72pk, 2025-07-13-12-55-54-cx5mhk.

🔥
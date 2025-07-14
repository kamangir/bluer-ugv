# bluer_swallow: digital: dataset: combination: one

```bash
@swallow dataset download

@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    sequence=3 . \
    --datasets $(@list filter \
	$(@swallow dataset list ~download) \
    --contains 2025-07-13)

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```

set:::object_name swallow-dataset-2025-07-14-09-03-36-crhuaq

assets:::get:::object_name/grid.png

🔥
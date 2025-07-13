# bluer_swallow: Dataset Combination

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    count=2 .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```

set:::object_name swallow-dataset-2025-07-11-13-03-58-aoadib

| | |
|-|-|
| assets:::get:::object_name/grid-000.png | assets:::get:::object_name/grid-001.png |

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name
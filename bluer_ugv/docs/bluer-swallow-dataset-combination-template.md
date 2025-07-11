# [Bluer Swallow](./bluer-swallow.md): Dataset Combination

```bash
@select swallow-dataset-$(@@timestamp)

@swallow dataset combine \
    count=2 .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```

set:::object_name swallow-dataset-2025-07-11-pggr4c

| | |
|-|-|
| assets:::get:::object_name/grid-00.png | assets:::get:::object_name/grid-01.png |

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name
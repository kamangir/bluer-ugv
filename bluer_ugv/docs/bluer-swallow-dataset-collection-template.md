# [Bluer Swallow](./bluer-swallow.md): Dataset Collection

```bash
@select swallow-dataset-$(@@timestamp)

@swallow dataset collect \
    count=2 .

@download - .
@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```

set:::object_name swallow-dataset-2025-07-11-qd39b2

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name
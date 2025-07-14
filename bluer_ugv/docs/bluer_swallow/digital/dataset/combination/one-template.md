# bluer_swallow: digital: dataset: combination: one

uses [collection/one](../collection/one.md).

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    sequence=3 . \
    --datasets $(@list filter \
	$(@swallow dataset list) \
    --contains 2025-07-13)

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```

set:::object_name swallow-dataset-2025-07-14-09-39-22-bfm9sx

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name
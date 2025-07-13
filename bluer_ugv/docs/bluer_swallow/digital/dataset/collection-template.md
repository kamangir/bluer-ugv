# bluer_swallow: digital: dataset: collection

Start `swallow`, press `t` (to start training), drive for 5 minutes, press `i` (to exit).

```bash
@select
@session start
```

```bash
@select 2025-07-09-10-26-30-itpbmu

@download - .
@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```

set:::object_name 2025-07-09-10-26-30-itpbmu

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name
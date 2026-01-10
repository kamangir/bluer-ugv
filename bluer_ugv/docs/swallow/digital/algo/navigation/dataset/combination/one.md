# swallow: digital: algo: navigation: dataset: combination: one

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


![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-14-09-39-22-bfm9sx/grid.png?raw=true)

[swallow-dataset-2025-07-14-09-39-22-bfm9sx.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-dataset-2025-07-14-09-39-22-bfm9sx.tar.gz)

```yaml
{}

```

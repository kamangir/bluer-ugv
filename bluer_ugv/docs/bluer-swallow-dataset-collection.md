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


![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-qd39b2/grid.png?raw=true)

[swallow-dataset-2025-07-11-qd39b2](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-dataset-2025-07-11-qd39b2.tar.gz)

```yaml
{}

```

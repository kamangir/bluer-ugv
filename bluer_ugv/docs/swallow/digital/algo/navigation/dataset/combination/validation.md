# swallow: digital: algo: navigation: dataset: combination: validation

uses [collection/validation](../collection/validation.md).

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    count=2 .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-13-03-58-aoadib/grid-000.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-13-03-58-aoadib/grid-001.png?raw=true) |

![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-13-03-58-aoadib/grid.png?raw=true)

[swallow-dataset-2025-07-11-13-03-58-aoadib.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-dataset-2025-07-11-13-03-58-aoadib.tar.gz)

```yaml
{}

```

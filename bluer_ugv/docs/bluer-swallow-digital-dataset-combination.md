# [Bluer Swallow](./bluer-swallow.md): Dataset Combination

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
| ![image](https://github.com/kamangir/assets/blob/main/TBA/grid-000.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/TBA/grid-001.png?raw=true) |

![image](https://github.com/kamangir/assets/blob/main/TBA/grid.png?raw=true)

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

```yaml
{}

```

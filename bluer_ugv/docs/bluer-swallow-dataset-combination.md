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
| ![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-10-48-45-hknrcf/grid-000.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-10-48-45-hknrcf/grid-001.png?raw=true) |

![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-10-48-45-hknrcf/grid.png?raw=true)

[swallow-dataset-2025-07-11-10-48-45-hknrcf](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-dataset-2025-07-11-10-48-45-hknrcf.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: no_action
    1: left
    2: right
  contains:
  - 2025-07-09-11-16-52-4zo4zc
  - 2025-07-09-11-34-19-bcoh75
  count: 1801
  shape:
  - 100
  - 100
  - 3
  subsets:
    eval: 0
    test: 0
    train: 1801

```

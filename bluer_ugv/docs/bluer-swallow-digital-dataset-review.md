# [Bluer Swallow](./bluer-swallow.md): Dataset Review

```bash
@select 2025-07-09-10-26-30-itpbmu

@algo dataset review - .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
@assets publish \
    extensions=png,push . \
    --prefix timeline
```


![image](https://github.com/kamangir/assets/blob/main/2025-07-09-10-26-30-itpbmu/grid.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/2025-07-09-10-26-30-itpbmu/timeline.png?raw=true)

[2025-07-09-10-26-30-itpbmu](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-07-09-10-26-30-itpbmu.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: no_action
    1: left
    2: right
  count: 283
  shape:
  - 100
  - 100
  - 3
  source: 00000000c74cf7d2
  subsets:
    eval: 0
    test: 0
    train: 283

```

# [Bluer Swallow](./bluer-swallow.md): Training

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    count=2 .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid

@select swallow-model-$(@timestamp)

@image_classifier model train - .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-13-05-02-u4z1ea/grid.png?raw=true)

[swallow-dataset-2025-07-11-13-05-02-u4z1ea](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-dataset-2025-07-11-13-05-02-u4z1ea.tar.gz)

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
    eval: 153
    test: 166
    train: 1482

```

---


![image](https://github.com/kamangir/assets/blob/main/TBA/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/TBA/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/TBA/confusion_matrix.png?raw=true)

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

```yaml
{}

```

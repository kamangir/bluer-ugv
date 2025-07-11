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


![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-13-17-59-6gw0fa/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-13-17-59-6gw0fa/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-13-17-59-6gw0fa/confusion_matrix.png?raw=true)

[swallow-model-2025-07-11-13-17-59-6gw0fa](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-11-13-17-59-6gw0fa.tar.gz)

```yaml
model:
  dataset:
    class_count: 3
    classes:
      0: no_action
      1: left
      2: right
    count: 1801
    shape:
    - 100
    - 100
    - 3
  evaluation:
    class_accuracy:
      0: 0.0
      1: 0.8987341772151899
      2: 0.234375
    eval_accuracy: 0.5620915032679739
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 0.8878281680356797
    - 0.8739532368224964
    - 0.8651033347113091
    - 0.8579061863876065
    - 0.8534764865471123
    - 0.8445938190950556
    - 0.8410894870758057
    - 0.8506735705653665
    - 0.8398284189775084
    - 0.8393932400766494

```

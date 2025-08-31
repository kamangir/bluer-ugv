# bluer-swallow: digital: algo: autonomous-driving: model: validation

uses [combination/validation](../dataset/combination/validation.md).

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    count=2 .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid

@select swallow-model-$(@timestamp)

@image_classifier model train upload .. .

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


![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-15-04-03-2glcch/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-15-04-03-2glcch/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-15-04-03-2glcch/confusion_matrix.png?raw=true)

[swallow-model-2025-07-11-15-04-03-2glcch](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-11-15-04-03-2glcch.tar.gz)

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
      1: 0.7341772151898734
      2: 0.65625
    eval_accuracy: 0.6535947712418301
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 0.8941771462861343
    - 0.8678298002956045
    - 0.8598417815891838
    - 0.863602487181845
    - 0.8459089610740723
    - 0.8423866080208186
    - 0.8415681831588951
    - 0.8320272445035206
    - 0.8420564680286103
    - 0.8336275264962643

```

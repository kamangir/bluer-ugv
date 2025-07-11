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


![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-13-08-10-0r76xx/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-13-08-10-0r76xx/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-13-08-10-0r76xx/confusion_matrix.png?raw=true)

[swallow-model-2025-07-11-13-08-10-0r76xx](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-11-13-08-10-0r76xx.tar.gz)

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
      1: 0.6329113924050633
      2: 0.6875
    eval_accuracy: 0.6143790849673203
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 0.8878798119613195
    - 0.8720086298169073
    - 0.866308025824718
    - 0.8579544165999944
    - 0.8534131259248968
    - 0.845552036556316
    - 0.8495868539359728
    - 0.841295415895027
    - 0.8341982520704488
    - 0.8353225727152085

```

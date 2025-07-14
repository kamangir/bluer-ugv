# bluer_swallow: digital: model: one

uses [collection/one](../dataset/combination/one.md).

🔥

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    sequence=3 . \
    --datasets $(@list filter \
        $(@swallow dataset list) \
        --contains 2025-07-13)

@assets publish \
    extensions=png,push . \
    --prefix grid

@select swallow-model-$(@timestamp)

@image_classifier model train upload .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```

---


![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-14-11-26-50-ap9cec/grid.png?raw=true)

```yaml
dataset:
  class_count: 3
  classes:
    0: no_action
    1: left
    2: right
  contains:
  - 2025-07-13-10-15-29-46j4oy
  - 2025-07-13-10-37-12-d4iwpm
  - 2025-07-13-12-55-54-cx5mhk
  count: 1749
  shape:
  - 100
  - 300
  - 3
  subsets:
    eval: 178
    test: 160
    train: 1411

```

---


![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-27-15-wup0ob/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-27-15-wup0ob/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-27-15-wup0ob/confusion_matrix.png?raw=true)

[swallow-model-2025-07-14-11-27-15-wup0ob](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-14-11-27-15-wup0ob.tar.gz)

```yaml
model:
  dataset:
    class_count: 3
    classes:
      0: no_action
      1: left
      2: right
    count: 1749
    shape:
    - 100
    - 300
    - 3
  evaluation:
    class_accuracy:
      0: 0.0
      1: 0.8990825688073395
      2: 0.3888888888888889
    eval_accuracy: 0.6685393258426966
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 0.9067365726116783
    - 0.8599148281367428
    - 0.8553446277416319
    - 0.8482238539223296
    - 0.8348034395975563
    - 0.8252276370577741
    - 0.8184360103519313
    - 0.8154178091729473
    - 0.8033121723304143
    - 0.8018080028635994

```

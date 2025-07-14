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

@image_classifier model train upload .. . \
    --num_epochs 4

@upload public,zip .
@assets publish \
    extensions=png,push .
```



---

![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-14-11-35-35-upbipx/grid.png?raw=true)

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
    eval: 186
    test: 169
    train: 1394

```

---

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-36-00-xmfhex/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-36-00-xmfhex/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-36-00-xmfhex/confusion_matrix.png?raw=true)

[swallow-model-2025-07-14-11-36-00-xmfhex](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-14-11-36-00-xmfhex.tar.gz)

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
      1: 0.9734513274336283
      2: 0.125
    eval_accuracy: 0.6290322580645161
  inputs:
    batch_size: 16
    num_epochs: 4
    object_name: swallow-dataset-2025-07-14-11-35-35-upbipx
  training:
    loss:
    - 0.8757732006877532
    - 0.8540839981742021
    - 0.8502828465985773
    - 0.8281957316432828

```

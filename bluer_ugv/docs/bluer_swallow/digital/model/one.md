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
    --num_epochs 40

@upload public,zip .
@assets publish \
    extensions=png,push .
```



---

![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-14-11-42-23-vsgfh1/grid.png?raw=true)

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
    eval: 187
    test: 159
    train: 1403

```

---

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-42-49-xeox1d/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-42-49-xeox1d/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-42-49-xeox1d/confusion_matrix.png?raw=true)

[swallow-model-2025-07-14-11-42-49-xeox1d](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-14-11-42-49-xeox1d.tar.gz)

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
      1: 0.953125
      2: 0.64
    eval_accuracy: 0.8235294117647058
  inputs:
    batch_size: 16
    num_epochs: 40
    object_name: swallow-dataset-2025-07-14-11-42-23-vsgfh1
  training:
    loss:
    - 0.8916369050380084
    - 0.8819582035349508
    - 0.8745246298467781
    - 0.868374662023736
    - 0.8626421864807648
    - 0.8583807032701379
    - 0.8458676740941369
    - 0.839448237495599
    - 0.8301841949278002
    - 0.8267826126969379
    - 0.8222294342322428
    - 0.8161937279609468
    - 0.8137866334667057
    - 0.8064358067444538
    - 0.8104829703665425
    - 0.8054575132881839
    - 0.800420668961232
    - 0.792694916873002
    - 0.8137895758034753
    - 0.7963057310344998
    - 0.7996092044873826
    - 0.7919924555297247
    - 0.7845326530364098
    - 0.7871585495541628
    - 0.8057369152223393
    - 0.7862884617667494
    - 0.7759614771634277
    - 0.7685270509546515
    - 0.7597933962187083
    - 0.7715578315008222
    - 0.7635332583446461
    - 0.7585970485796694
    - 0.7502197460540261
    - 0.7372843822409915
    - 0.7679044849432458
    - 0.7166859915616762
    - 0.7179099483653127
    - 0.7029619025317414
    - 0.6854000445866874
    - 0.6888541663364266

```

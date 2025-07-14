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

![image](https://github.com/kamangir/assets/blob/main/{}/grid.png?raw=true)

```yaml
{}

```

---

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-31-01-wzbq76/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-31-01-wzbq76/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-11-31-01-wzbq76/confusion_matrix.png?raw=true)

[swallow-model-2025-07-14-11-31-01-wzbq76](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-14-11-31-01-wzbq76.tar.gz)

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
      1: 0.9108910891089109
      2: 0.30158730158730157
    eval_accuracy: 0.6453488372093024
  inputs:
    batch_size: 16
    num_epochs: 20
  training:
    loss:
    - 0.9025775203127987
    - 0.8702159845666878
    - 0.8615187929200546
    - 0.8584252891151412
    - 0.8463460803885244
    - 0.8375800983685635
    - 0.8252031873103629
    - 0.8119564908013313
    - 0.8086788177319569
    - 0.8284006517276478
    - 0.8022296512519451
    - 0.8064591539870353
    - 0.7974561142255856
    - 0.7975125567948895
    - 0.7919459233731138
    - 0.7872894254000424
    - 0.7877603093470176
    - 0.7789561152884853
    - 0.7782923688441409
    - 0.7943609629517039

```

# bluer-swallow: digital: algo: navigation: model: validation

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


![image](https://github.com/kamangir/assets/blob/main//loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main//evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main//confusion_matrix.png?raw=true)

[](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/.tar.gz)

```yaml
api_count: 2167
created_by: bluer_geo-5.15.1-bluer_flow-5.16.1-bluer_ai-12.136.1-bluer_objects-6.96.1-bluer_options-5.86.1-torch-2.2.2-Python
  3.12.9-Darwin 23.6.0--Jupyter-Notebook
creation_date: 23 April 2025, 10:33:49
dataset:
  class_count: 10
  classes:
    0: Apple 8
    1: Apple Braeburn 1
    2: Apple Golden 1
    3: Apple hit 1
    4: Cactus fruit red 1
    5: Cherry 4
    6: Nut 3
    7: Pear Red 1
    8: Tomato Cherry Orange 1
    9: Zucchini 1
  count: 10
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 2
    test: 0
    train: 8
description: Civilian Harm in Ukraine TimeMap
failure_count: 0
ingested_count: 2167
range:
- 2022-02-24
- 2025-04-06

```

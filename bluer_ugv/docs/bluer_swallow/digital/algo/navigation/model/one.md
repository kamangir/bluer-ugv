# bluer-swallow: digital: algo: navigation: model: one

uses [combination/one](../dataset/combination/one.md).


```bash
@arvan ssh <ip-address>
@arvan seed
# Ctrl+V
```

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    sequence=3 . \
    --datasets $(@list filter \
        $(@swallow dataset list) \
        --contains 2025-07-13)

@upload filename=metadata.yaml .
@assets publish \
    extensions=png,push . \
    --prefix grid

@select swallow-model-$(@timestamp)

@image_classifier model train upload .. . \
    --num_epochs 100

@upload public,zip .
@assets publish \
    extensions=png,push .

@select swallow-prediction-test-$(@timestamp)

@algo image_classifier model prediction_test \
    upload ... .. .

@assets publish \
    extensions=png,push .
```




---

![image](https://github.com/kamangir/assets/blob/main/{}/grid.png?raw=true)


<details>
<summary>metadata</summary>

```yaml
{}

```

</details>


---

![image](https://github.com/kamangir/assets/blob/main//loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main//evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main//confusion_matrix.png?raw=true)

[](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/.tar.gz)


<details>
<summary>metadata</summary>

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

</details>


---

![image](https://github.com/kamangir/assets/blob/main/swallow-prediction-test-2025-07-14-14-13-57-ngywj1/prediction.png?raw=true)


<details>
<summary>metadata</summary>

```yaml
prediction:
  elapsed_time: 0.39812374114990234
  predicted_class: 2

```

</details>


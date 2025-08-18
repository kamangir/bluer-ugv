# bluer_swallow: digital: model: one

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

![image](https://github.com/kamangir/assets/blob/main/BLUER_UGV_SWALLOW_MODEL/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/BLUER_UGV_SWALLOW_MODEL/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/BLUER_UGV_SWALLOW_MODEL/confusion_matrix.png?raw=true)

[BLUER_UGV_SWALLOW_MODEL](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/BLUER_UGV_SWALLOW_MODEL.tar.gz)


<details>
<summary>metadata</summary>

```yaml
{}

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


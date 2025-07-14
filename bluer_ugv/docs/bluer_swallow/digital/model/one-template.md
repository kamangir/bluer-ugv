title:::

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

set:::model_object_name swallow-model-2025-07-14-13-18-10-kx0qrw

set:::prediction_object_name swallow-prediction-test-2025-07-14-14-13-57-ngywj1

set:::dataset_object_name metadata:::get:::model_object_name:::model.inputs.object_name

---

assets:::get:::dataset_object_name/grid.png

details:::metadata
metadata:::get:::dataset_object_name
details:::

---

assets:::get:::model_object_name/loss.png

assets:::get:::model_object_name/evaluation.png

assets:::get:::model_object_name/confusion_matrix.png

object:::get:::model_object_name

details:::metadata
metadata:::get:::model_object_name
details:::

---

assets:::get:::prediction_object_name/prediction.png

details:::metadata
metadata:::get:::prediction_object_name
details:::
title:::

uses [collection/one](../dataset/combination/one.md).


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

@assets publish \
    extensions=png,push . \
    --prefix grid

@select swallow-model-$(@timestamp)

@image_classifier model train upload .. . \
    --num_epochs 100

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::model_object_name swallow-model-2025-07-14-09-35-16-7q7h82

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
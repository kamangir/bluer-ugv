title:::

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

set:::dataset_object_name swallow-dataset-2025-07-14-11-26-50-ap9cec

assets:::get:::dataset_object_name/grid.png

metadata:::get:::dataset_object_name

---

set:::model_object_name swallow-model-2025-07-14-11-27-15-wup0ob

assets:::get:::model_object_name/loss.png

assets:::get:::model_object_name/evaluation.png

assets:::get:::model_object_name/confusion_matrix.png

object:::get:::model_object_name

metadata:::get:::model_object_name
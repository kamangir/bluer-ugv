# [Bluer Swallow](./bluer-swallow.md): Training

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    count=2,recent .

@upload public,zip .
@assets publish \
    extensions=png,push .

@select swallow-model-$(@timestamp)

@image_classifier model train - .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::dataset_object_name TBA

assets:::get:::dataset_object_name/grid.png

object:::get:::dataset_object_name

metadata:::get:::dataset_object_name

---

set:::model_object_name TBA

assets:::get:::model_object_name/loss.png

assets:::get:::model_object_name/evaluation.png

assets:::get:::model_object_name/confusion_matrix.png

object:::get:::model_object_name

metadata:::get:::model_object_name
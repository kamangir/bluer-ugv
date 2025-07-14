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

![image](https://github.com/kamangir/assets/blob/main/{}/grid.png?raw=true)

```yaml
{}

```

---

![image](https://github.com/kamangir/assets/blob/main/TBA/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/TBA/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/TBA/confusion_matrix.png?raw=true)

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

```yaml
{}

```

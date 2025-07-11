# [Bluer Swallow](./bluer-swallow.md): Training

```bash
@select swallow-dataset-$(@timestamp)

@swallow dataset combine \
    count=2,recent,split .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid

@select swallow-model-$(@timestamp)

@image_classifier model train - .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/TBA/grid.png?raw=true)

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

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

# swallow: digital: algo: navigation: model: validation

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

[swallow-dataset-2025-07-11-13-05-02-u4z1ea.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-dataset-2025-07-11-13-05-02-u4z1ea.tar.gz)

```yaml
{}

```

---


![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-15-04-03-2glcch/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-15-04-03-2glcch/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-11-15-04-03-2glcch/confusion_matrix.png?raw=true)

[swallow-model-2025-07-11-15-04-03-2glcch.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-11-15-04-03-2glcch.tar.gz)

```yaml
{}

```

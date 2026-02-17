# swallow: digital: algo: navigation: model: one

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



set:::dataset_object_name swallow-dataset-2025-07-14-13-16-51-ajhuvd

---

![image](https://github.com/kamangir/assets/blob/main/swallow-dataset-2025-07-11-13-05-02-u4z1ea/grid.png?raw=true)


<details>
<summary>metadata</summary>

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

</details>


---

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-13-18-10-kx0qrw/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-13-18-10-kx0qrw/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/swallow-model-2025-07-14-13-18-10-kx0qrw/confusion_matrix.png?raw=true)

[swallow-model-2025-07-14-13-18-10-kx0qrw.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/swallow-model-2025-07-14-13-18-10-kx0qrw.tar.gz)


<details>
<summary>metadata</summary>

```yaml
model:
  dataset:
    class_count: 3
    classes:
      0: no_action
      1: left
      2: right
    count: 1749
    shape:
    - 100
    - 300
    - 3
  evaluation:
    class_accuracy:
      0: 0.0
      1: 0.883495145631068
      2: 0.7857142857142857
    eval_accuracy: 0.7934782608695652
  inputs:
    batch_size: 16
    num_epochs: 100
    object_name: swallow-dataset-2025-07-14-13-16-51-ajhuvd
  training:
    loss:
    - 0.8877076580904533
    - 0.8598213399665943
    - 0.8321751488291699
    - 0.8361254111580226
    - 0.8165319940318232
    - 0.810976495431817
    - 0.8174320357433263
    - 0.8049073198567266
    - 0.8042267538499142
    - 0.8037144360334977
    - 0.8106899869614753
    - 0.7936147969702015
    - 0.7975053638651751
    - 0.7990057148795197
    - 0.7844245243763578
    - 0.7806977004244707
    - 0.7979188764440841
    - 0.7904210748879806
    - 0.7762736838796864
    - 0.7712624143863069
    - 0.77167194062385
    - 0.7753188591072525
    - 0.7661490410998247
    - 0.7658116072848223
    - 0.7765054495438285
    - 0.7586202873699907
    - 0.7527277478273364
    - 0.7513948983040408
    - 0.7557499035545018
    - 0.7440192365128061
    - 0.749240611774334
    - 0.7425943602686343
    - 0.731538266375445
    - 0.7310858128727347
    - 0.7376282287680584
    - 0.7270766672880753
    - 0.7157144525776739
    - 0.7176215043102485
    - 0.714605612685715
    - 0.7071798699489539
    - 0.7123250064642533
    - 0.7029482817304307
    - 0.696342456686324
    - 0.7141255855560302
    - 0.6992517054080963
    - 0.6798342849897302
    - 0.6731243372827337
    - 0.6893571252408235
    - 0.6668049086695133
    - 0.6679666450058205
    - 0.6740042050679524
    - 0.675813958696697
    - 0.6724764763445094
    - 0.6578732815341674
    - 0.6555768227231675
    - 0.6354364196459452
    - 0.6337134278338888
    - 0.6373340093571207
    - 0.6223556299140488
    - 0.6243257505306299
    - 0.6260139499885449
    - 0.5986429368240246
    - 0.6137995635253796
    - 0.6102780635806098
    - 0.61760830430017
    - 0.5824633577595586
    - 0.5780590316523676
    - 0.5733150862265324
    - 0.6104433524435845
    - 0.5775181599285292
    - 0.559887102721394
    - 0.5568356574445531
    - 0.560498204956884
    - 0.5401299799697986
    - 0.5470088523367177
    - 0.5846111666465151
    - 0.5379512375679569
    - 0.5437732660252115
    - 0.5317604545233906
    - 0.527497600040574
    - 0.5273767986159393
    - 0.5122150310571643
    - 0.5082207786864129
    - 0.5092103229052779
    - 0.513486811734628
    - 0.4963915469205898
    - 0.5050811750733334
    - 0.4847544426503389
    - 0.49197240134944087
    - 0.4857381089873936
    - 0.47842193967190344
    - 0.4811662900275078
    - 0.4893507706946221
    - 0.47012589858925863
    - 0.49397963436617365
    - 0.4673444630443186
    - 0.4526644229888916
    - 0.46080744197403173
    - 0.4754720388979152
    - 0.4501733610595482

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


# swallow: digital: algo: yolo: train

training a `256 x 256` model.

# ingest

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest - . \
    --classes person

@yolo dataset review \
    ~download .

@upload public,zip

@assets publish \
    extensions=png,push .
```


[coco128-2025-09-16-ko2aq9.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/coco128-2025-09-16-ko2aq9.tar.gz)

![image](https://github.com/kamangir/assets/blob/main/coco128-2025-09-16-ko2aq9/review.png?raw=true)

```yaml
{}

```

## train

```bash
@select coco128-model-$(@@timestamp)

@yolo model train \
    ~download,upload .. . \
    --epochs 20 \
    --image_size 256

@upload public,zip

@assets publish \
    extensions=jpg+png . \
    --prefix train/

@assets publish \
    extensions=jpg+png,push . \
    --prefix validation/
```


[coco128-model-2025-09-16-meb4if.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/coco128-model-2025-09-16-meb4if.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/results.png?raw=true) |

| | | | |
|-|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/BoxF1_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/BoxPR_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/BoxP_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/BoxR_curve.png?raw=true) |

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/confusion_matrix.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/confusion_matrix_normalized.png?raw=true) |

| | | |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/train_batch0.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/train_batch1.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/train_batch2.jpg?raw=true) |

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/val_batch0_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/val_batch0_pred.jpg?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/val_batch1_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/val_batch1_pred.jpg?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/val_batch2_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-16-meb4if/val_batch2_pred.jpg?raw=true) | 


<details>
<summary>metadata</summary>

```yaml
{}

```

</details>


## predict

```bash
@select yolo-prediction-test-$(@timestamp)

@yolo model prediction_test \
    upload \
    $BLUER_ALGO_COCO128_TEST_DATASET \
    $BLUER_UGV_SWALLOW_YOLO_MODEL . \
    --record_index 3

@assets publish extensions=png,push
```


![image](https://github.com/kamangir/assets/blob/main/yolo-prediction-test-2025-09-16-17-01-49-7s95jv/000000000389.png?raw=true)

```yaml
{}

```

## predict (256)

```bash
@select yolo-prediction-test-$(@timestamp)

@yolo model prediction_test \
    upload \
    $BLUER_ALGO_COCO128_TEST_DATASET \
    $BLUER_UGV_SWALLOW_YOLO_MODEL . \
    --record_index 3 \
    --image_size 256

@assets publish extensions=png,push
```


![image](https://github.com/kamangir/assets/blob/main/yolo-prediction-test-2025-09-16-17-02-49-yhwh85/000000000389.png?raw=true)

```yaml
{}

```

## predict (rpi)

```bash
@select swallow-debug-$(@timestamp)

@swallow debug .

@assets publish extensions=gif,push
```

|   |   |   |
| --- | --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-0.png?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-0.png?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-2.png?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-2.png?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-3.png?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-3.png?raw=true) |
| [![image](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-4.png?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-4.png?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-5.png?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/yolo-debug-5.png?raw=true) | [![image](https://github.com/kamangir/assets/raw/main/swallow-debug-2025-09-16-19-53-19-4yzsp8/swallow-debug-2025-09-16-19-53-19-4yzsp8-2.gif?raw=true)](https://github.com/kamangir/assets/raw/main/swallow-debug-2025-09-16-19-53-19-4yzsp8/swallow-debug-2025-09-16-19-53-19-4yzsp8-2.gif?raw=true) |

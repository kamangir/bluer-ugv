title:::


```bash
@select release-$(@timestamp)
@pdf convert - @ugv \
swallow,\
swallow/digital,\
swallow/digital/design,\
swallow/digital/design/parts.md,\
aliases/swallow.md,\
swallow/digital/algo,\
swallow/digital/algo/driving.md,\
swallow/digital/algo/navigation,\
swallow/digital/algo/navigation/dataset,\
swallow/digital/algo/navigation/dataset/collection,\
swallow/digital/algo/navigation/dataset/collection/validation.md,\
swallow/digital/algo/navigation/dataset/collection/one.md,\
swallow/digital/algo/navigation/dataset/review.md,\
swallow/digital/algo/navigation/dataset/combination,\
swallow/digital/algo/navigation/dataset/combination/validation.md\
swallow/digital/algo/navigation/dataset/combination/one.md\
swallow/digital/algo/navigation/model,\
swallow/digital/algo/navigation/model/validation.md,\
swallow/digital/algo/navigation/model/one.md,\
swallow/digital/algo/tracking,\
swallow/digital/algo/yolo,\
swallow/digital/algo/yolo/train.md,\
arzhang/design \
    .
@assets publish extensions=pdf,push .
```

set:::object_name TBA

assets:::get:::object_name/release.pdf
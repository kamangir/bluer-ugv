title:::


```bash
@select release-$(@timestamp)

@pdf convert - @ugv \
swallow,\
$abcli_path_git/bluer-designs/swallow/terminology.png,\
swallow/digital,\
swallow/digital/design,\
swallow/digital/design/parts.md,\
aliases/swallow.md,\
swallow/digital/design/parts.md,\
swallow/digital/design/terraform.md,\
swallow/digital/design/computer,\
$abcli_path_git/bluer-designs/swallow/electrical/digital.png,\
$abcli_path_git/bluer-designs/swallow/kicad/swallow/exports/swallow.pdf,\
$abcli_path_git/bluer-designs/swallow/kicad/swallow/exports/swallow-3d.png,\
$abcli_path_git/bluer-designs/swallow/kicad/swallow/exports/swallow-3d-back.png,\
$abcli_path_git/bluer-designs/swallow/kicad/swallow/exports/swallow-pcb.png,\
swallow/digital/design/rpi-pinout.md,\
swallow/digital/design/operation.md,\
swallow/digital/design/mechanical,\
$abcli_path_git/bluer-designs/swallow/mechanical/robot.png,\
$abcli_path_git/bluer-designs/swallow/mechanical/cage.png,\
$abcli_path_git/bluer-designs/swallow/mechanical/measurements.png,\
$abcli_path_git/bluer-designs/swallow/ultrasonic-sensors/geometry.png,\
swallow/digital/algo,\
swallow/digital/algo/driving.md,\
swallow/digital/algo/navigation,\
swallow/digital/algo/navigation/dataset,\
swallow/digital/algo/navigation/dataset/collection,\
swallow/digital/algo/navigation/dataset/collection/validation.md,\
swallow/digital/algo/navigation/dataset/collection/one.md,\
swallow/digital/algo/navigation/dataset/review.md,\
swallow/digital/algo/navigation/dataset/combination,\
swallow/digital/algo/navigation/dataset/combination/validation.md,\
swallow/digital/algo/navigation/dataset/combination/one.md,\
swallow/digital/algo/navigation/model,\
swallow/digital/algo/navigation/model/validation.md,\
swallow/digital/algo/navigation/model/one.md,\
swallow/digital/algo/tracking,\
swallow/digital/algo/yolo,\
swallow/digital/algo/yolo/train.md .

@pdf convert - @ugv \
arzhang,\
arzhang/design,\
arzhang/design/specs.md,\
arzhang/design/mechanical,\
$abcli_path_git/bluer-designs/arzhang/robot.png,\
$abcli_path_git/bluer-designs/arzhang/cage.png,\
$abcli_path_git/bluer-designs/arzhang/robot-with-cover.png,\
$abcli_path_git/bluer-designs/arzhang/measurements.png,\
arzhang/design/parts.md .

@pdf convert - @ugv \
validations,\
validations/timing-review.md,\
validations/village-1.md,\
validations/village-2.md,\
validations/village-3.md,\
validations/village-4.md,\
validations/village-5.md,\
validations/village-6.md,\
validations/village-7.md .

@pdf convert - @sbc \
swallow,\
swallow-head .

@pdf convert - @algo \
image_classifier,\
image_classifier/dataset,\
image_classifier/dataset/ingest.md,\
image_classifier/dataset/review.md,\
image_classifier/dataset/sequence.md,\
image_classifier/model,\
image_classifier/model/train,\
image_classifier/model/train/small.md,\
image_classifier/model/train/large.md,\
image_classifier/model/prediction,\
image_classifier/model/prediction/dev.md,\
image_classifier/model/prediction/rpi.md .

@pdf convert - @algo \
tracker,\
tracker/camshift.md,\
tracker/meanshift.md .

@pdf convert - @algo \
yolo,\
yolo/dataset,\
yolo/dataset/ingest-and-review.md,\
yolo/model,\
yolo/model/validation.md .

@pdf convert combine @algo \
bps,\
bps/literature.md,\
bps/mathematics,\
bps/mathematics/timing,\
bps/mathematics/localization.md,\
bps/validations,\
bps/validations/test-introspect.md,\
bps/validations/beacon-receiver.md,\
bps/validations/loop-2.md,\
bps/validations/loop-3.md,\
bps/validations/review.md,\
bps/validations/data-collection.md,\
bps/validations/live-1.md,\
bps/validations/live-2.md,\
bps/validations/live-2b.md,\
bps/validations/live-3.md,\
bps/simulations,\
bps/simulations/timing.md .

@upload filename=release.pdf .

@assets publish extensions=pdf,push .
```

set:::object_name release-2025-11-09-02-50-43-vkhs2k

assets:::get:::object_name/release.pdf
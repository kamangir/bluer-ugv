# releases: two


```bash
@select release-$(@timestamp)
@metadata edit - .

@metadata upload .

@pdf convert combine,~compress,~upload .

🔥

@assets publish extensions=pdf,push .
```


[release.pdf](https://github.com/kamangir/assets/blob/main/release-2025-11-30-22-48-03-uw8wwl/release.pdf)

```yaml
- bluer-ugv/bluer_ugv/docs/swallow
- bluer-designs/swallow/terminology.png
- bluer-ugv/bluer_ugv/docs/swallow/digital
- bluer-ugv/bluer_ugv/docs/swallow/digital/design
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/parts.md
- bluer-ugv/bluer_ugv/docs/aliases/swallow.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/parts.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/terraform.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/computer
- bluer-designs/swallow/electrical/digital.png
- bluer-designs/swallow/kicad/swallow/exports/swallow.pdf
- bluer-designs/swallow/kicad/swallow/exports/swallow-3d.png
- bluer-designs/swallow/kicad/swallow/exports/swallow-3d-back.png
- bluer-designs/swallow/kicad/swallow/exports/swallow-pcb.png
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/rpi-pinout.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/operation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/mechanical
- bluer-designs/swallow/mechanical/robot.png
- bluer-designs/swallow/mechanical/cage.png
- bluer-designs/swallow/mechanical/measurements.png
- bluer-designs/swallow/ultrasonic-sensors/geometry.png
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/driving.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/collection
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/collection/validation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/collection/one.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/review.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/combination
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/combination/validation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/combination/one.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/model
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/model/validation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/model/one.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/tracking
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/yolo
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/yolo/train.md
- bluer-ugv/bluer_ugv/docs/arzhang
- bluer-ugv/bluer_ugv/docs/arzhang/design
- bluer-ugv/bluer_ugv/docs/arzhang/design/specs.md
- bluer-ugv/bluer_ugv/docs/arzhang/design/mechanical
- bluer-designs/arzhang/robot.png
- bluer-designs/arzhang/cage.png
- bluer-designs/arzhang/robot-with-cover.png
- bluer-designs/arzhang/measurements.png
- bluer-ugv/bluer_ugv/docs/arzhang/design/power.md
- bluer-ugv/bluer_ugv/docs/validations
- bluer-ugv/bluer_ugv/docs/validations/timing-review.md
- bluer-ugv/bluer_ugv/docs/validations/village-1.md
- bluer-ugv/bluer_ugv/docs/validations/village-2.md
- bluer-ugv/bluer_ugv/docs/validations/village-3.md
- bluer-ugv/bluer_ugv/docs/validations/village-4.md
- bluer-ugv/bluer_ugv/docs/validations/village-5.md
- bluer-ugv/bluer_ugv/docs/validations/village-6.md
- bluer-ugv/bluer_ugv/docs/validations/village-7.md
- bluer-sbc/bluer_sbc/docs/swallow
- bluer-sbc/bluer_sbc/docs/swallow-head
- bluer-algo/bluer_algo/docs/image_classifier
- bluer-algo/bluer_algo/docs/image_classifier/dataset
- bluer-algo/bluer_algo/docs/image_classifier/dataset/ingest.md
- bluer-algo/bluer_algo/docs/image_classifier/dataset/review.md
- bluer-algo/bluer_algo/docs/image_classifier/dataset/sequence.md
- bluer-algo/bluer_algo/docs/image_classifier/model
- bluer-algo/bluer_algo/docs/image_classifier/model/train
- bluer-algo/bluer_algo/docs/image_classifier/model/train/small.md
- bluer-algo/bluer_algo/docs/image_classifier/model/train/large.md
- bluer-algo/bluer_algo/docs/image_classifier/model/prediction
- bluer-algo/bluer_algo/docs/image_classifier/model/prediction/dev.md
- bluer-algo/bluer_algo/docs/image_classifier/model/prediction/rpi.md
- bluer-algo/bluer_algo/docs/tracker
- bluer-algo/bluer_algo/docs/tracker/camshift.md
- bluer-algo/bluer_algo/docs/tracker/meanshift.md
- bluer-algo/bluer_algo/docs/yolo
- bluer-algo/bluer_algo/docs/yolo/dataset
- bluer-algo/bluer_algo/docs/yolo/dataset/ingest-and-review.md
- bluer-algo/bluer_algo/docs/yolo/model
- bluer-algo/bluer_algo/docs/yolo/model/validation.md
- bluer-algo/bluer_algo/docs/bps
- bluer-algo/bluer_algo/docs/bps/literature.md
- bluer-algo/bluer_algo/docs/bps/mathematics
- bluer-algo/bluer_algo/docs/bps/mathematics/timing
- bluer-algo/bluer_algo/docs/bps/mathematics/localization.md
- bluer-algo/bluer_algo/docs/bps/validations
- bluer-algo/bluer_algo/docs/bps/validations/test-introspect.md
- bluer-algo/bluer_algo/docs/bps/validations/beacon-receiver.md
- bluer-algo/bluer_algo/docs/bps/validations/loop-2.md
- bluer-algo/bluer_algo/docs/bps/validations/loop-3.md
- bluer-algo/bluer_algo/docs/bps/validations/review.md
- bluer-algo/bluer_algo/docs/bps/validations/data-collection.md
- bluer-algo/bluer_algo/docs/bps/validations/live-1.md
- bluer-algo/bluer_algo/docs/bps/validations/live-2.md
- bluer-algo/bluer_algo/docs/bps/validations/live-2b.md
- bluer-algo/bluer_algo/docs/bps/validations/live-3.md
- bluer-algo/bluer_algo/docs/bps/simulations
- bluer-algo/bluer_algo/docs/bps/simulations/timing.md

```

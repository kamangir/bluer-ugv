# releases: two


```bash
@select release-two-$(@timestamp)
cp -v $(python3 -m bluer_ugv locate)/docs/releases/two.yaml ./metadata.yaml

@pdf convert combine,upload .

@assets publish extensions=pdf,push .
```


[release.pdf](https://github.com/kamangir/assets/blob/main/release-two-2025-12-01-12-50-03-1hyrts/release.pdf)


<details>
<summary>metadata</summary>

pdf:
```yaml
- bluer-ugv
- bluer-algo
- bluer-sbc
- bluer-ai
- bluer-designs/swallow/terminology.png
- bluer-sbc/bluer_sbc/docs/swallow
- bluer-sbc/bluer_sbc/docs/swallow-head
- bluer-ugv/bluer_ugv/docs/swallow
- bluer-ugv/bluer_ugv/docs/aliases/swallow.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/parts.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/terraform.md
- bluer-ai/bluer_ai/docs/install/RPi.md
- bluer-designs/swallow/electrical/digital.png
- bluer-designs/swallow/kicad/swallow/exports/swallow.pdf
- bluer-designs/swallow/kicad/swallow/exports/swallow-3d.png
- bluer-designs/swallow/kicad/swallow/exports/swallow-3d-back.png
- bluer-designs/swallow/kicad/swallow/exports/swallow-pcb.png
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/computer/box.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/computer/testing.md
- bluer-sbc/bluer_sbc/docs/adapter-bus.md
- bluer-sbc/bluer_sbc/docs/regulated-bus.md
- bluer-sbc/bluer_sbc/docs/battery-bus.md
- bluer-sbc/bluer_sbc/docs/pwm-generator.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/computer/power.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/computer/naming.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/rpi-pinout.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/operation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/mechanical
- bluer-designs/swallow/mechanical/robot.png
- bluer-designs/swallow/mechanical/cage.png
- bluer-designs/swallow/mechanical/measurements.png
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/ultrasonic-sensor/dev.md
- bluer-designs/swallow/ultrasonic-sensors/geometry.png
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/testing.md
- bluer-ugv/bluer_ugv/docs/arzhang
- bluer-ugv/bluer_ugv/docs/arzhang/design/specs.md
- bluer-ugv/bluer_ugv/docs/arzhang/design/mechanical
- bluer-designs/arzhang/robot.png
- bluer-designs/arzhang/cage.png
- bluer-designs/arzhang/robot-with-cover.png
- bluer-designs/arzhang/measurements.png
- bluer-ugv/bluer_ugv/docs/arzhang/design/power.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/driving.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/collection/validation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/collection/one.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/review.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/combination/validation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/combination/one.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/model/validation.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/model/one.md
- bluer-algo/bluer_algo/docs/aliases/image_classifier.md
- bluer-algo/bluer_algo/docs/image_classifier/dataset/ingest.md
- bluer-algo/bluer_algo/docs/image_classifier/dataset/review.md
- bluer-algo/bluer_algo/docs/image_classifier/dataset/sequence.md
- bluer-algo/bluer_algo/docs/image_classifier/model/train/small.md
- bluer-algo/bluer_algo/docs/image_classifier/model/train/large.md
- bluer-algo/bluer_algo/docs/image_classifier/model/prediction/dev.md
- bluer-algo/bluer_algo/docs/image_classifier/model/prediction/rpi.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/tracking
- bluer-algo/bluer_algo/docs/aliases/tracker.md
- bluer-algo/bluer_algo/docs/tracker
- bluer-algo/bluer_algo/docs/tracker/camshift.md
- bluer-algo/bluer_algo/docs/tracker/meanshift.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/yolo
- bluer-ugv/bluer_ugv/docs/swallow/digital/algo/yolo/train.md
- bluer-algo/bluer_algo/docs/aliases/yolo.md
- bluer-algo/bluer_algo/docs/yolo/dataset/ingest-and-review.md
- bluer-algo/bluer_algo/docs/yolo/model/validation.md
- bluer-algo/bluer_algo/docs/bps
- bluer-algo/bluer_algo/docs/aliases/bps.md
- bluer-algo/bluer_algo/docs/bps/literature.md
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
- bluer-algo/bluer_algo/docs/bps/simulations/timing.md
- bluer-algo/bluer_algo/docs/aliases/socket.md
- bluer-algo/bluer_algo/docs/socket.md
- bluer-ugv/bluer_ugv/docs/validations
- bluer-ugv/bluer_ugv/docs/validations/timing-review.md
- bluer-ugv/bluer_ugv/docs/validations/village-1.md
- bluer-ugv/bluer_ugv/docs/validations/village-2.md
- bluer-ugv/bluer_ugv/docs/validations/village-3.md
- bluer-ugv/bluer_ugv/docs/validations/village-4.md
- bluer-ugv/bluer_ugv/docs/validations/village-5.md
- bluer-ugv/bluer_ugv/docs/validations/village-6.md
- bluer-ugv/bluer_ugv/docs/validations/village-7.md
- bluer-objects
- bluer-options
- bluer-south
- bluer-sandbox
- bluer-geo
- bluer-flow
- bluer-plugin
- giza
- giza/pdf/giza.pdf

```

ignore:
```yaml
- bluer-ai/bluer_ai/docs/aliases
- bluer-ai/bluer_ai/docs/install
- bluer-flow
- bluer-geo
- bluer-objects
- bluer-plugin
- bluer-sandbox
- bluer-sbc/bluer_sbc/docs/aliases/camera.md
- bluer-sbc/bluer_sbc/docs/aliases/hardware.md
- bluer-sbc/bluer_sbc/docs/aliases/rpi.md
- bluer-sbc/bluer_sbc/docs/aliases/rpi.md
- bluer-sbc/bluer_sbc/docs/aliases/sbc.md
- bluer-sbc/bluer_sbc/docs/bryce.md
- bluer-sbc/bluer_sbc/docs/cheshmak.md
- bluer-sbc/bluer_sbc/docs/nafha
- bluer-sbc/bluer_sbc/docs/parts
- bluer-sbc/bluer_sbc/docs/shelter
- bluer-sbc/bluer_sbc/docs/ultrasonic-sensor-tester.md
- bluer-ugv/bluer_ugv/docs/aliases/ugv.md
- bluer-ugv/bluer_ugv/docs/eagle
- bluer-ugv/bluer_ugv/docs/fire
- bluer-ugv/bluer_ugv/docs/rangin
- bluer-ugv/bluer_ugv/docs/ravin/ravin3
- bluer-ugv/bluer_ugv/docs/ravin/ravin4
- bluer-ugv/bluer_ugv/docs/releases
- bluer-ugv/bluer_ugv/docs/swallow/analog
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/computer/pcb.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/computer/schematics.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/steering-over-current-detection
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/ultrasonic-sensor/shield.md
- bluer-ugv/bluer_ugv/docs/swallow/digital/design/ultrasonic-sensor/tester.md
- bluer-ugv/bluer_ugv/docs/UGVs

```

</details>


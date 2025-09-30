# aliases: swallow

## dataset

```bash
@swallow \
	dataset \
	combine \
	[count=<count>,~download,~recent,sequence=<3>,~split,upload] \
	[-|<object-name>] \
	[--datasets <object-name-1>+<object-name-2>] \
	[--test_ratio 0.1] \
	[--train_ratio 0.8]
 . combine swallow datasets.
@swallow \
	dataset \
	download \
	[~metadata,navigation|yolo]
 . download the swallow dataset.
@swallow \
	dataset \
	edit \
	[~download,navigation|yolo]
 . edit the swallow dataset.
@swallow \
	dataset \
	list \
	[~download,navigation|yolo]
 . list the swallow dataset.
@swallow \
	dataset \
	upload \
	[~metadata,navigation|yolo]
 . upload the swallow dataset.
```

## env

```bash
@swallow \
	env \
	cp \
	[<env-name>]
 . cp swallow swallow-raspbian-<env-name>.env.
@swallow \
	env \
	list
 . list swallow envs.
@swallow \
	env \
	set \
	steering \
	0 | 1
 . set env.
   steering: BLUER_SBC_SWALLOW_HAS_STEERING
```

## ultrasonic-sensor

```bash
@swallow \
	ultrasonic \
	test \
	[~upload] \
	[-|<object-name>] \
	[--export 0] \
	[--log 0] \
	[--max_m 0.8]
 . test ultrasonic sensors.
```

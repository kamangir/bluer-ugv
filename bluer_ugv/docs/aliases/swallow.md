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

## debug

```bash
@swallow \
	debug \
	[~upload] \
	[-|<object-name>] \
	[--generate_gif 0] \
	[--save_images 0]
 . debug swallow.
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
	bps | full_keyboard | steering \
	0 | 1
 . set env.
   bps: BLUER_SBC_SWALLOW_HAS_BPS (currently: 0)
   full_keyboard: BLUER_SBC_SWALLOW_HAS_FULL_KEYBOARD (currently: 0)
   steering: BLUER_SBC_SWALLOW_HAS_STEERING (currently: 1)
```

## keyboard

```bash
@swallow \
	keyboard \
	test \
	[dryrun] \
	[--keys 1234567890-+/.]
 . test keyboard.
```

## select-target

```bash
@swallow \
	select_target \
	[--host <hostname>] \
	[--loop 0]
 . select swallow target.
```

## ultrasonic-sensor

```bash
@swallow \
	ultrasonic \
	review \
	[~download,upload] \
	[.|<object-name>] \
	[--frame_count <-1>] \
	[--gif 0] \
	[--rm_blank 0]
 . review ultrasonic sensor data.
@swallow \
	ultrasonic \
	test \
	[~upload] \
	[-|<object-name>] \
	[--export 0] \
	[--frame_count <-1>] \
	[--gif 0] \
	[--log 0] \
	[--max_m 0.80] \
	[--rm_blank 0]
 . test ultrasonic sensors.
```

## video

```bash
@swallow \
	video_player \
	pause
 . pause video player.
@swallow \
	video_player \
	play \
	[download,video=<loading|1>] \
	[rangin-video-list-1|<object-name>]
 . play <object-name>.
@swallow \
	video \
	playlist \
	cat \
	[download]
 . cat swallow playlist.
@swallow \
	video \
	playlist \
	download
 . download swallow playlist.
@swallow \
	video \
	playlist \
	edit \
	[download]
 . edit swallow playlist.
@swallow \
	video \
	playlist \
	upload
 . upload swallow playlist.
@swallow \
	video_player \
	stop
 . stop video player.
```

# aliases: ugv

```bash
@ugv \
	build_README \
	[push]
 . build @ugv/README.md.
@ugv \
	pypi \
	browse \
	[token]
 . browse pypi/@ugv.
@ugv \
	pypi \
	build \
	[browse,install,~rm_dist,~upload]
 . build pypi/@ugv.
@pypi \
	install
 . install pypi.
@ugv \
	pylint \
	[ignore=<ignore>] \
	[<args>]
 . pylint @ugv.
@ugv \
	pytest \
	[list,dryrun,~log,show_warning,~verbose] \
	[filename.py|filename.py::test]
 . pytest @ugv.
@ugv \
	test \
	[what=all|<test-name>,dryrun] \
	[dryrun]
 . test @ugv.
@ugv \
	test \
	list
 . list @ugv tests.
@ugv \
	git \
	[designs]
 . @git @ugv.
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
@swallow \
	debug \
	[~upload] \
	[-|<object-name>] \
	[--generate_gif 0] \
	[--save_images 0]
 . debug swallow.
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
@swallow \
	select_target \
	[--host <hostname>] \
	[--loop 0]
 . select swallow target.
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

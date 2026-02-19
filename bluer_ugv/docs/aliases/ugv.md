# aliases: ugv

```bash
@ugv \
	build_README \
	[ai,push,root=<root>]
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
	get \
	<ugv-name> \
	computers.back | computers.front | computers.top | <what>
 . get ugv info.
@ugv \
	git \
	[designs]
 . @git @ugv.
@ROS \
	install \
	[dryrun]
 . install ROS.
@ROS \
	start \
	[dryrun]
 . start ROS.
@ugv \
	ssh \
	<ugv-name> \
	[back | front | top | <node>]
 . ssh to <ugv-name>.<node>
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
	cat \
	[<env-name>]
 . cat swallow-raspbian-<env-name>.env.
@swallow \
	env \
	cd
 . cd env folder.
@swallow \
	env \
	cp \
	[<env-name>]
 . cp swallow-raspbian-<env-name>.env.
@swallow \
	env \
	list
 . list swallow envs.
@swallow \
	env \
	set \
	bps | camera | dev_mode | full_keyboard | screen | steering \
	0 | 1
 . set env.
   bps: BLUER_SBC_SWALLOW_HAS_BPS (currently: 0)
   camera: BLUER_SBC_SWALLOW_HAS_CAMERA (currently: 1)
   dev_mode: BLUER_SBC_SWALLOW_DEV_MODE (currently: 1)
   full_keyboard: BLUER_SBC_SWALLOW_HAS_FULL_KEYBOARD (currently: 0)
   screen: BLUER_SBC_ENABLE_SCREEN (currently: 1)
   steering: BLUER_SBC_SWALLOW_HAS_STEERING (currently: 1)
@swallow \
	ethernet \
	test \
	[dryrun] \
	[--is_server 0 | 1] \
	[--server_name 0.0.0.0 | <server_name>.local]
 . test ethernet.
@swallow \
	git \
	rm_keys \
	[~dryrun,undo]
 . (undo) rm github keys.
@swallow \
	keyboard \
	test \
	[dryrun] \
	[--keys 1234567890-+/.]
 . test keyboard.
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
@swallow \
	video \
	play \
	[--dryrun 1] \
	[--download 0] \
	[--engine mpv | vlc] \
	[--loop 0] \
	[--object_name <rangin-video-list-1>] \
	[--timeout <-1 | 10>] \
	[--video <loading|1>]
 . play <object-name>/<video>.
@swallow \
	video \
	playlist \
	cat \
	[download]
 . cat swallow playlist.
@swallow \
	video \
	playlist \
	download \
	[filename=<filename>,policy=different|doesnt_exist|none]
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
	upload \
	[filename=<filename>,public,zip]
 . upload swallow playlist.
@ugv \
	watch \
	<ugv-name> \
	[back | front | top | <node>]
 . watch <ugv-name>.<node>.
```

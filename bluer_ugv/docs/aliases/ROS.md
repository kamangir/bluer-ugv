# aliases: ROS

```bash
@ROS \
	gazebo \
	log
 . log the state.
@ROS \
	gazebo \
	gui \
	open \
	[dryrun]
 . open gazebo gui.
@ROS \
	gazebo \
	gui \
	serve \
	[dryrun]
 . serve gazebo gui.
@ROS \
	gazebo \
	control \
	[angular=<0.0>,linear=<0.0>,partition=arzhang4]
 . control the robot.
   angular: rotational velocity (rad/s)
   linear: forward/backward velocity (m/s)
@ROS \
	gazebo \
	robot \
	publish \
	[partition=arzhang4]
 . publish robot description.
@ROS \
	gazebo \
	robot \
	spawn \
	[partition=arzhang4]
 . spawn robot.
@ROS \
	install \
	[dryrun]
 . install ROS.
@ROS \
	open \
	[dryrun]
 . open ROS.
@ROS \
	package \
	build \
	<package-name> \
	[dryrun]
 . build package.
@ROS \
	package \
	create \
	<package-name> \
	[dryrun]
 . create package.
@ROS \
	package \
	rm \
	<package-name> \
	[dryrun]
 . rm package.
@ROS \
	start \
	[build,~cache,dryrun]
 . start ROS.
@ROS \
	stop \
	[dryrun]
 . stop ROS.
@ROS \
	test \
	[doctor,gazebo,gpio,dryrun,role=talker|listener]
 . test ROS.
```

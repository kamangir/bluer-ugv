# aliases: ROS

```bash
@arzhang4 \
	run \
	[~build,dryrun] \
	<node-name>]
 . run <node-name>.
   node-name: motor_driver | teleop
@arzhang4 \
	test \
	[~build,dryrun] \
	<node-name>
 . test <node-name>.
   node-name: teleop
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
	log
 . log the state.
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

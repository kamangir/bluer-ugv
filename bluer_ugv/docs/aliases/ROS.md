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
	[angular=<0.0>,dryrun,linear=<0.0>]
 . control the robot.
   angular
      rotational velocity (rad/s)
   linear
      forward/backward velocity (m/s)
@ROS \
	gazebo \
	robot \
	publish \
	[dryrun]
 . publish robot description.
@ROS \
	gazebo \
	robot \
	spawn \
	[dryrun]
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
	start \
	[build,~cache,dryrun]
 . start ROS.
@ROS \
	stop \
	[dryrun]
 . stop ROS.
@ROS \
	test \
	[doctor,dryrun,role=talker|listener]
 . test ROS.
```

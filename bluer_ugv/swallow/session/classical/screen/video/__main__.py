import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ugv import NAME
from bluer_ugv.swallow.session.classical.screen.video.playlist import PlayList
from bluer_ugv.swallow.session.classical.screen.video.player import VideoPlayer
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="pause|play|stop",
)
parser.add_argument(
    "--download",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--dryrun",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--video",
    type=int,
)
args = parser.parse_args()

video_player = VideoPlayer(args.dryrun == 1)

success = False
if args.task == "pause":
    success = video_player.pause()
elif args.task == "play":
    playlist = PlayList(args.object_name)

    success = video_player.pause()

    success = func(args.arg)
elif args.task == "stop":
    success = video_player.stop()
else:
    success = None

sys_exit(logger, NAME, args.task, success)

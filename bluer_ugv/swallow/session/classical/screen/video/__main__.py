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
    default=1,
    help="0|1",
)
parser.add_argument(
    "--dryrun",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--loop",
    type=int,
    default=1,
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
    playlist = PlayList(
        args.object_name,
        download=args.download == 1,
    )

    success = video_player.play(
        filename=playlist.get(args.video),
        loop=args.loop == 1,
    )
elif args.task == "stop":
    success = video_player.stop()
else:
    success = None

sys_exit(logger, NAME, args.task, success)

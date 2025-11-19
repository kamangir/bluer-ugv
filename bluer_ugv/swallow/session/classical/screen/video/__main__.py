import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_options.host import is_rpi, is_headless

from bluer_ugv import NAME, env
from bluer_ugv.swallow.session.classical.screen.video.playlist import PlayList
from bluer_ugv.swallow.session.classical.screen.video.player import VideoPlayer
from bluer_ugv.swallow.session.classical.screen.video.player import VideoPlayerEngine
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="play",
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
    default=int(not is_rpi() or is_headless()),
    help="0|1",
)
parser.add_argument(
    "--engine",
    type=str,
    default=VideoPlayerEngine.VLC.name.lower(),
    help=" | ".join(sorted([engine.name.lower() for engine in VideoPlayerEngine])),
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
    default=env.RANGIN_VIDEO_LIST_OBJECT,
)
parser.add_argument(
    "--video",
    type=str,
    default="loading",
)
args = parser.parse_args()


success = False
if args.task == "play":
    playlist = PlayList(
        args.object_name,
        download=args.download == 1,
    )

    video_player = VideoPlayer(
        args.dryrun == 1,
        engine=VideoPlayerEngine[args.engine.upper()],
    )

    success = video_player.play(
        filename=playlist.get(args.video),
        loop=args.loop == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)

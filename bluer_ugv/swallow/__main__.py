import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ugv import NAME
from bluer_ugv.swallow.targeting import select_target
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="select_target",
)
parser.add_argument(
    "--host",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "select_target":
    success = select_target(args.host)
else:
    success = None

sys_exit(logger, NAME, args.task, success)

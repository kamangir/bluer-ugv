import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ugv import NAME
from bluer_ugv.socket.testing import test_receiving, test_sending
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="test",
)
parser.add_argument(
    "--what",
    type=str,
    default="receiving",
    help="receiving | sending",
)
parser.add_argument(
    "--host",
    type=str,
    default="",
)
args = parser.parse_args()

success = False
if args.task == "test":
    success = (
        test_receiving()
        if args.what == "receiving"
        else test_sending(args.host) if args.what == "sending" else False
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)

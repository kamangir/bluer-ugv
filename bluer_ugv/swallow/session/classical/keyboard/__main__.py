import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ugv import NAME
from bluer_ugv.swallow.session.classical.keyboard.testing import test
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="test",
)
parser.add_argument(
    "--keys",
    type=str,
    default=" ",
    help="star=*",
)
args = parser.parse_args()

success = False
if args.task == "test":
    success = test(list_of_keys="*" if args.keys == "star" else args.keys)
else:
    success = None

sys_exit(logger, NAME, args.task, success)

import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ugv import NAME
from bluer_ugv.help.swallow.env import dict_of_variables
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="get_var_name",
)
parser.add_argument(
    "--keyword",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "get_var_name":
    success = True
    print(
        dict_of_variables.get(args.keyword, {}).get(
            "name",
            "",
        )
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)

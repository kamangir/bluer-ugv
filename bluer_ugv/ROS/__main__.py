import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ugv import NAME
from bluer_ugv.ROS.rsp_yaml import generate_rsp_yaml
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="generate_rsp_yaml",
)
parser.add_argument(
    "--urdf_path",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "generate_rsp_yaml":
    success = generate_rsp_yaml(
        urdf_path=args.urdf_path,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)

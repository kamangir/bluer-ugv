import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_ugv import env
from bluer_ugv import NAME
from bluer_ugv.swallow.session.classical.ethernet.client import EthernetClient
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="test",
)
parser.add_argument(
    "--is_server",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--server_name",
    type=str,
    default="0.0.0.0",
    help="0.0.0.0 | <server_name>.local",
)
args = parser.parse_args()

success = False
if args.task == "test":
    success = True
    client = EthernetClient(
        host=args.server_name,
        port=env.BLUER_UGV_ETHERNET_PORT,
        is_server=args.is_server == 1,
    )

    try:
        while True:
            client.process()
    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")
    except Exception as e:
        logger.error(e)
        success = False

    client.close()
else:
    success = None

sys_exit(logger, NAME, args.task, success)

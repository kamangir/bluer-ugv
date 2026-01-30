import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_options.env import abcli_hostname

from bluer_ugv import env
from bluer_ugv import NAME
from bluer_ugv.README.ugvs.ethernet import find_server
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
    "--arg",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "test":
    success, is_server, server_name = find_server(hostname=abcli_hostname)
    if success:
        client = EthernetClient(
            host=server_name,
            port=env.BLUER_UGV_ETHERNET_PORT,
            is_server=is_server,
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

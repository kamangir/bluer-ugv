from typing import Union, Dict

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.ethernet.command import EthernetCommand
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint


class ClassicalEthernetSetPoint(ClassicalSetPoint):
    def put(
        self,
        value: Union[int, bool, Dict[str, Union[int, bool]]],
        what: str = "all",
        log: bool = True,
        steering_expires_in: float = env.BLUER_UGV_SWALLOW_STEERING_EXPIRY_ETHERNET,
    ):
        super().put(
            value=value,
            what=what,
            log=log,
            steering_expires_in=steering_expires_in,
        )

        self.ethernet.client.send(
            EthernetCommand(
                action="setpoint.put",
                data={
                    "value": value,
                    "what": what,
                    "log": log,
                    "steering_expires_in": steering_expires_in,
                },
            )
        )

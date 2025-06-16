from bluer_ugv.swallow.session.classical.motor.generic import GenericMotor
from bluer_ugv.swallow.session.classical.mousepad import ClassicalMousePad


class RearMotors(GenericMotor):
    def __init__(
        self,
        mousepad: ClassicalMousePad,
    ):
        super().__init__(
            role="speed",
            lpwm_pin=19,
            rpwm_pin=13,
            mousepad=mousepad,
        )

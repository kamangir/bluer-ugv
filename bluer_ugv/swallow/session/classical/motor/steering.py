from bluer_ugv.swallow.session.classical.motor.generic import GenericMotor
from bluer_ugv.swallow.session.classical.mousepad import ClassicalMousePad


class SteeringMotor(GenericMotor):
    def __init__(
        self,
        mousepad: ClassicalMousePad,
    ):
        super().__init__(
            role="steering",
            mousepad=mousepad,
        )

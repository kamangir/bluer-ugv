from bluer_ugv.swallow.session.classical.motor.generic import GenericMotor
from bluer_ugv.swallow.session.classical.setpoint import ClassicalSetPoint


class ClassicalSteeringMotor(GenericMotor):
    def __init__(
        self,
        setpoint: ClassicalSetPoint,
    ):
        super().__init__(
            role="steering",
            lpwm_pin=12,
            rpwm_pin=18,
            setpoint=setpoint,
        )

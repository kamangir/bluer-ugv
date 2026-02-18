from bluer_ugv.README.swallow.digital.design.arzhang4 import docs as arzhang4
from bluer_ugv.README.swallow.digital.design import (
    ethernet,
    joystick,
    mechanical,
    obsolete,
    operation,
    parts,
    terraform,
    testing,
    ultrasonic_sensor,
)


docs = (
    [
        {
            "path": "../docs/swallow/digital/design",
        },
        {
            "path": "../docs/swallow/digital/design/rpi-pinout.md",
        },
    ]
    + arzhang4.docs
    + ethernet.docs
    + joystick.docs
    + mechanical.docs
    + obsolete.docs
    + operation.docs
    + parts.docs
    + terraform.docs
    + testing.docs
    + ultrasonic_sensor.docs
)

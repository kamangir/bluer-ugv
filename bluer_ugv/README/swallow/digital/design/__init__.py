from bluer_ugv.README.swallow.digital.design import (
    arzhang4,
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

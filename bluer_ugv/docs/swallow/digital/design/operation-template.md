title:::

## keyboard

keys:::

*: special key.

to enable full keyboard:

```bash
@swallow env set full_keyboard 1
```

the range of numpad is ~10-20 m range, noticeably lower than that of the full keyboard, which is ~50 m, see [village-6](../../../validations/village-6.md) for details.


items:::

## leds
    - green: control loop.
    - red:
        - flashing:
            - motor update.
            - action / training.
            - release the push button to update.
            - setpoint update.
        - solid: release the push button to shutdown.
    - yellow: 
        - command received. 
        - mousepad activity.
    - blue: ultrasonic sensor echo.

details:::mouse pad (obsolete)
## mouse pad

⚠️ obsolete

    - move your finger:
        - vertically: adjust speed.
        - horizontally: set steering.
    - double click: stop.

details:::

## push button

    - hold for 5 seconds: update.
    - hold for 10 seconds: shutdown.
    - hold for > 15 seconds: skip.

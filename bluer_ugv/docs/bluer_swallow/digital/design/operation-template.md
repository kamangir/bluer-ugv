title:::

- keyboard:
    -  a: steer left.
    -  b: debug on.
    - zb: debug off. 
    -  d: steer right.
    -  g: mode = prediction.
    - zi: exit.
    - zo: shutdown.
    -  s: speed backward.
    - zp: reboot.
    -  t: mode = train.
    - zu: update.
    -  w: speed forward.
    -  y: mode = none.
    - space: stop.

items:::

- leds:
    - green: control loop.
    - red:
        - flashing:
            - motor update.
            - prediction / training.
            - release the push button to update.
            - setpoint update.
        - solid: release the push button to shutdown.
    - yellow: 
        - command received. 
        - mousepad activity.
    - blue: ultrasonic sensor echo.

- mouse pad: 
    - move your finger:
        - vertically: adjust speed.
        - horizontally: set steering.
    - double click: stop.

- push button:
    - hold for 5 seconds: update.
    - hold for 10 seconds: shutdown.
    - hold for > 15 seconds: skip.

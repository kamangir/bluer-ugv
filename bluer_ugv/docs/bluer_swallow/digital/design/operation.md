# bluer-swallow: digital: design: operation

- keyboard:
    - a: steer left.
    - d: steer right.
    - g: mode = prediction.
    - i: exit.
    - o: shutdown.
    - s: speed backward.
    - p: reboot.
    - t: mode = train.
    - u: update.
    - w: speed forward.
    - y: mode = none.
    - space: stop.

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

# bluer-swallow: digital: design: operation

- keyboard:
    -  a: steer left.
    -  b: debug on.
    -  d: steer right.
    -  g: mode = prediction.
    - zi: exit.
    -  m: ultrasonic sensor disabled.
    -  n: ultrasonic sensor enabled.
    - zo: shutdown.
    -  s: speed backward.
    - zp: reboot.
    -  t: mode = train.
    - zu: update.
    -  v: debug off. 
    -  w: speed forward.
    -  y: mode = none.
    - space: stop.

|   |
| --- |
| [![image](https://github.com/kamangir/assets2/raw/main/bluer-swallow/20251005_113232.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/bluer-swallow/20251005_113232.jpg?raw=true) |

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

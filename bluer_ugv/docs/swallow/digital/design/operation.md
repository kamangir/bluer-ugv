# swallow: digital: design: operation

## keyboard

| event | full keyboard | numpad |
|-|-|-|
 | debug off | v | 9 | 
 | debug on | b | 7 | 
 | exit | *i | *7 | 
 | mode = action | g | 1 | 
 | mode = none | y | 5 | 
 | mode = training | t | 3 | 
 | reboot | *p | *5 | 
 | shutdown | *o | *9 | 
 | special key | z | . | 
 | speed backward | s | 2 | 
 | speed forward | w | 8 | 
 | steer left | a | 4 | 
 | steer right | d | 6 | 
 | stop |   | 0 | 
 | ultrasonic off | n | - | 
 | ultrasonic on | m | + | 
 | update | *u | *1 | 

*: special key.

to enable full keyboard:

```bash
@swallow env set full_keyboard 1
```

the range of numpad is ~10-20 m range, noticeably lower than that of the full keyboard, which is ~50 m, see [village-6](../../../validations/village-6.md) for details.


|   |   |
| --- | --- |
| [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251019_121811.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251019_121811.jpg?raw=true) | [![image](https://github.com/kamangir/assets2/raw/main/swallow/20251019_121842.jpg?raw=true)](https://github.com/kamangir/assets2/raw/main/swallow/20251019_121842.jpg?raw=true) |

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


<details>
<summary>mouse pad (obsolete)</summary>

## mouse pad

⚠️ obsolete

    - move your finger:
        - vertically: adjust speed.
        - horizontally: set steering.
    - double click: stop.


</details>


## push button

    - hold for 5 seconds: update.
    - hold for 10 seconds: shutdown.
    - hold for > 15 seconds: skip.

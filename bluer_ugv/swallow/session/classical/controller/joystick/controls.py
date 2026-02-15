from typing import Dict

Controls: Dict[str, Dict] = {
    "axes": {
        3: ("speed", -1),
        2: ("steering", 1),
    },
    "buttons": {
        9: "ultrasonic off",
        7: "ultrasonic on",
        8: "debug off",
        6: "debug on",
        3: "mode = none",
        0: "mode = action",
        1: "mode = training",
        12: "special key",
        14: "stop",
    },
    "special-buttons": {
        0: "exit",
        1: "shutdown",
        3: "reboot",
        4: "update",
    },
}

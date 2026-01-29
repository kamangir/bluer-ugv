from typing import Dict


class EthernetCommand:
    def __init__(self):
        self.action: str = ""
        self.data: Dict = {}

    def as_str(self) -> str:
        return "{}({})[{}]".format(
            self.__class__.__name__,
            self.action,
            self.data,
        )

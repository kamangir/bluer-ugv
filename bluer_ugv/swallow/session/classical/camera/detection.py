class Detection:
    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        confidence: float = 0.0,
        area: float = 0.0,
    ):
        self.x: float = x
        self.y: float = y
        self.confidence: float = confidence
        self.area: float = area

    def as_str(self) -> str:
        return "{} @[{:.2f},{:.2f}](C:{:.2f}%,A:{:.2f}%)".format(
            self.__class__.__name__,
            self.x,
            self.y,
            self.confidence * 100,
            self.area * 100,
        )

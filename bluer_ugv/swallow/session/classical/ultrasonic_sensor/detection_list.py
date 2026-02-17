from typing import List, Iterable, Iterator

from bluer_ugv.swallow.session.classical.config.state import State
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import Detection


class DetectionList:
    def __init__(
        self,
        list_of_detections: Iterable[Detection] | None = None,
    ):
        self._content: List[Detection] = (
            list(list_of_detections) if list_of_detections else []
        )

    def __iter__(self) -> Iterator[Detection]:
        return iter(self._content)

    def __len__(self) -> int:
        return len(self._content)

    def __getitem__(self, index: int) -> Detection:
        return self._content[index]

    def append(self, detection: Detection) -> None:
        self._content.append(detection)

    def as_str(
        self,
        short: bool = False,
    ) -> List[str]:
        return [detection.as_str(short=short) for detection in self._content]

    @property
    def state(self) -> State:
        if any(detection.state == State.DANGER for detection in self._content):
            return State.DANGER

        if any(detection.state == State.WARNING for detection in self._content):
            return State.WARNING

        return State.CLEAR

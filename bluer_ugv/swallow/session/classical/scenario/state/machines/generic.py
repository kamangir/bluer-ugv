from typing import List

from bluer_ugv.swallow.session.classical.keyboard.classes import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.camera.generic import ClassicalCamera
from bluer_ugv.swallow.session.classical.scenario.state.generic import GenericState
from bluer_ugv.swallow.session.classical.scenario.state.starting import StartingState
from bluer_ugv.logger import logger


class GenericStateMachine:
    name = "generic"

    def __init__(
        self,
        keyboard: ClassicalKeyboard,
        camera: ClassicalCamera,
    ):
        self.keyboard = keyboard
        self.camera = camera

        self.list_of_states: List[GenericState] = [
            StartingState(
                keyboard=self.keyboard,
                camera=self.camera,
            ),
        ]
        self.index: int = 0

        self.load()

    @property
    def state(self) -> GenericState:
        return self.list_of_states[self.index]

    def load(self) -> bool:
        logger.info(
            "loaded {}: [{}] - state: {}".format(
                self.__class__.__name__,
                ", ".join([state.name for state in self.list_of_states]),
                self.state.name,
            )
        )
        return self.state.open()

    def process(self) -> bool:
        if self.index < 0 or self.index > len(self.list_of_states) - 1:
            logger.error(
                "{}.process: bad state: {}, expected [{},{}]".format(
                    self.__class__.__name__,
                    self.index,
                    0,
                    len(self.list_of_states) - 1,
                )
            )
            return False

        if not self.state.process():
            return False

        try:
            change, next_state_name = self.list_of_states[
                self.index
            ].decide_state_change()
        except Exception as e:
            logger.error(e)
            return False

        if not change:
            return True

        if next_state_name not in [state.name for state in self.list_of_states]:
            logger.error(
                "{}.process: {}: state not found in {}".format(
                    self.__class__.__name__,
                    next_state_name,
                    ", ".join([state.name for state in self.list_of_states]),
                )
            )
            return False

        if not self.state.close():
            return False

        old_index = self.index
        self.index = [state.name for state in self.list_of_states].index(
            next_state_name
        )

        if not self.state.open():
            return False

        logger.info(
            '{}.process: state #{} "{}" -> state #{} "{}"'.format(
                self.__class__.__name__,
                old_index,
                self.list_of_states[old_index].name,
                self.index,
                self.state.name,
            )
        )
        return True

    def stop(self):
        self.state.close()
        logger.info(f"{self.__class__.__name__}.stop")

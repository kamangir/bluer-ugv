from bluer_sbc.imager.camera import instance as camera
from bluer_options.timer import Timer
from bluer_options import string

from bluer_ugv.swallow.session.classical.keyboard import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv import env
from bluer_ugv.logger import logger


class ClassicalCamera:
    def __init__(
        self,
        keyboard: ClassicalKeyboard,
        leds: ClassicalLeds,
        object_name: str,
    ):
        self.timer = Timer(
            period=env.BLUER_UGV_CAMERA_PERIOD,
            name=self.__class__.__name__,
        )

        self.keyboard = keyboard
        self.leds = leds

        self.object_name = object_name

        # create the dataset

    def initialize(self) -> bool:
        return camera.open(log=True)

    def cleanup(self):
        camera.close(log=True)

        # save dataset

    def update(self) -> bool:
        if any(
            [
                self.keyboard.train_mode,
                self.timer.tick(),
                self.keyboard.last_key != "",
            ]
        ):
            return True

        self.leds.leds["red"]["state"] = not self.leds.leds["red"]["state"]

        filename = "{}.png".format(
            string.pretty_date(
                as_filename=True,
                unique=True,
            )
        )

        success, _ = camera.capture(
            close_after=False,
            open_before=False,
            object_name=self.object_name,
            filename=filename,
            log=True,
        )
        if not success:
            return success

        # dataset +=

        self.timer.reset()

        return True

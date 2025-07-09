from bluer_sbc.imager.camera import instance as camera

from bluer_ugv.logger import logger


class ClassicalCamera:
    def initialize(self) -> bool:
        return camera.open(log=True)

    def cleanup(self):
        camera.close(log=True)

    def update(self) -> bool:
        return True

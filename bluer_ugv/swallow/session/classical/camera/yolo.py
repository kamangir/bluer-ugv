from typing import List
import numpy as np

from bluer_options.timer import Timer
from bluer_options import string
from bluer_options import host
from bluer_objects.storage.policies import DownloadPolicy
from bluer_objects import storage
from bluer_objects.metadata import post_to_object, get_from_object
from bluer_sbc.imager.camera import instance as camera
from bluer_algo.yolo.dataset.classes import YoloDataset
from bluer_algo.yolo.model.predictor import YoloPredictor

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.camera.generic import ClassicalCamera
from bluer_ugv.swallow.session.classical.keyboard import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv.swallow.session.classical.mode import OperationMode
from bluer_ugv.logger import logger


class ClassicalYoloCamera(ClassicalCamera):
    def __init__(
        self,
        keyboard: ClassicalKeyboard,
        leds: ClassicalLeds,
        setpoint: ClassicalSetPoint,
        object_name: str,
    ):
        super().__init__(keyboard, leds, setpoint, object_name)

        self.prediction_timer = Timer(
            period=env.BLUER_UGV_CAMERA_ACTION_PERIOD,
            name="{}.prediction".format(self.__class__.__name__),
            log=True,
        )
        self.training_timer = Timer(
            period=env.BLUER_UGV_CAMERA_TRAINING_PERIOD,
            name="{}.training".format(self.__class__.__name__),
            log=True,
        )

        self.dataset = YoloDataset(
            object_name=self.object_name,
            create=True,
        )

        self.predictor = None

        self.action_enabled: bool = True

    def initialize(self) -> bool:
        if not super().initialize():
            return False

        if not storage.download(
            env.BLUER_UGV_SWALLOW_YOLO_MODEL,
            policy=DownloadPolicy.DOESNT_EXIST,
        ):
            return False

        success, self.predictor = YoloPredictor.load(
            object_name=env.BLUER_UGV_SWALLOW_YOLO_MODEL,
        )
        return success

    def cleanup(self):
        super().cleanup()

        self.dataset.save(
            verbose=True,
        )

        if self.dataset.empty:
            return

        dataset_list: List[str] = get_from_object(
            object_name=env.BLUER_UGV_SWALLOW_YOLO_DATASET_LIST,
            key="dataset-list",
            default=[],
            download=True,
        )
        dataset_list.append(self.object_name)
        if not post_to_object(
            object_name=env.BLUER_UGV_SWALLOW_YOLO_DATASET_LIST,
            key="dataset-list",
            value=dataset_list,
            upload=True,
            verbose=True,
        ):
            logger.error("failed to add object to dataset list.")

    def update(self) -> bool:
        if self.keyboard.mode == OperationMode.ACTION:
            self.setpoint.put(
                what="steering",
                value=0,
                log=True,
            )

        if not super().update():
            return False

        if self.keyboard.mode == OperationMode.ACTION:
            return self.update_action()

        if self.keyboard.mode == OperationMode.TRAINING:
            return self.update_training()

        return True

    def update_action(self) -> bool:
        self.action_enabled = not self.action_enabled

        if not self.prediction_timer.tick() or not self.action_enabled:
            return True

        self.leds.leds["red"]["state"] = not self.leds.leds["red"]["state"]

        success, image = camera.capture(
            close_after=False,
            open_before=False,
            log=True,
        )
        if not success:
            return success

        success, metadata = self.predictor.predict(
            image=image,
        )
        if not success:
            return success

        if not metadata["detections"]:
            logger.info("no detections.")
            return True

        detection_off_center = [
            (
                (detection["bbox_xyxy"][0] + detection["bbox_xyxy"][2]) / 2
                - image.shape[1] / 2
            )
            ** 2
            + (
                (detection["bbox_xyxy"][1] + detection["bbox_xyxy"][3]) / 2
                - image.shape[0] / 2
            )
            ** 2
            for detection in metadata["detections"]
        ]

        detection_index_list = [
            index
            for index in range(len(detection_off_center))
            if detection_off_center[index] == min(detection_off_center)
        ]
        detection_index = detection_index_list[0]
        logger.info(
            "taking detection #{}: off-center: {} px".format(
                detection_index,
                detection_off_center[detection_index] ** 0.5,
            )
        )

        detection = metadata["detections"][detection_index]
        detection_y_center = (detection["bbox_xyxy"][1] + detection["bbox_xyxy"][3]) / 2
        if detection_y_center > image.shape[0] / 2:
            self.setpoint.put(
                what="steering",
                value=env.BLUER_UGV_SWALLOW_STEERING_SETPOINT,
                log=True,
            )
        else:
            self.setpoint.put(
                what="steering",
                value=-env.BLUER_UGV_SWALLOW_STEERING_SETPOINT,
                log=True,
            )

        return True

    def update_training(self) -> bool:
        if not (self.training_timer.tick() or self.keyboard.last_key != ""):
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

        # TODO: dataset +=

        self.training_timer.reset()

        return True

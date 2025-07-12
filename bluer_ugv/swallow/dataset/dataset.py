from typing import Dict, Tuple, cast
import re
import datetime
import matplotlib.pyplot as plt

from bluer_objects import file, objects
from bluer_objects.graphics.signature import justify_text
from bluer_algo.image_classifier.dataset.dataset import ImageClassifierDataset

from bluer_ugv.host import signature
from bluer_ugv.logger import logger


class ImageDataset(ImageClassifierDataset):
    def generate_timeline(
        self,
        log: bool = True,
        line_width: int = 80,
    ) -> bool:
        df = self.df.copy()

        pattern = re.compile(r"(\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})-[a-z0-9]+\.png")

        if not df["filename"].apply(lambda x: bool(pattern.fullmatch(x))).all():
            logger.warning("Not all filenames match the expected timestamp pattern.")
            return True

        df["datetime"] = df["filename"].apply(
            lambda x: datetime.strptime(
                pattern.match(x).group(1),
                "%Y-%m-%d-%H-%M-%S",
            )
        )

        df = df.sort_values(by="datetime")

        plt.figure(figsize=(10, 4))
        plt.plot(df["datetime"], df["class_index"], marker="o")
        plt.title(
            justify_text(
                " | ".join(
                    objects.signature(object_name=self.object_name) + self.signature()
                ),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.xlabel(
            justify_text(
                " | ".join(["label"] + signature()),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.ylabel("label")
        plt.title("Class Index Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

        return file.save_fig(
            objects.path_of(
                object_name=self.object_name,
                filename="timeline.png",
            ),
            log=log,
        )

    @classmethod
    def load(
        cls,
        object_name: str,
        log: bool = True,
        visual_log: bool = True,
    ) -> Tuple[bool, "ImageDataset"]:
        success, dataset = super().load(
            object_name=object_name,
            log=log,
            visual_log=visual_log,
        )
        if not success:
            return success

        dataset = cast(ImageDataset, dataset)

        if visual_log:
            if not dataset.generate_timeline(log=log):
                return False, dataset

        return True, dataset

    def save(
        self,
        metadata: Dict = {},
        log: bool = True,
    ) -> bool:
        if not super().save(
            metadata=metadata,
            log=log,
        ):
            return False

        return self.generate_timeline()

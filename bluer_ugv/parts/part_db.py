from typing import List, Union, Dict
import copy

from blueness import module
from bluer_objects import README

from bluer_ugv import NAME
from bluer_ugv.parts.part import Part
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


class PartDB:
    def __init__(self):
        self._db: Dict[str, Part] = {}

    def __iter__(self):
        return iter(self._db.values())

    def __setitem__(
        self,
        name: str,
        part: Union[Part, List[str]],
    ):
        if isinstance(part, list):
            part = Part(
                name=name,
                info=part,
            )
        else:
            part.name = name

        self._db[name] = copy.deepcopy(part)

    def __getitem__(self, name: str) -> Part:
        return self._db[name]

    @property
    def README(self) -> List[str]:
        return sorted(
            [
                "- [{}](./{}.md).".format(
                    part.info[0],
                    part.name,
                )
                for part in self
            ]
        )

    def adjust(
        self,
        dryrun: bool = True,
    ) -> bool:
        logger.info(
            "{}.adjust{}".format(
                NAME,
                " [dryrun]" if dryrun else "",
            )
        )

        return True

        images = []
        max_width = 0
        max_height = 0

        # Step 1: Load all images and find max width/height
        for filename in os.listdir(path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                filepath = os.path.join(path, filename)
                img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)

                if img is None:
                    continue  # Skip unreadable files

                # Convert to 4-channel RGBA if not already
                if img.shape[2] == 3:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
                elif img.shape[2] == 1:
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)

                images.append((filename, img))
                h, w = img.shape[:2]
                max_width = max(max_width, w)
                max_height = max(max_height, h)

        # Step 2: Resize canvas for each image and save with new name
        for filename, img in images:
            h, w = img.shape[:2]
            new_img = np.zeros(
                (max_height, max_width, 4), dtype=np.uint8
            )  # Transparent by default

            # Compute top-left corner to center the image
            y_offset = (max_height - h) // 2
            x_offset = (max_width - w) // 2

            # Paste the image into center of new canvas
            new_img[y_offset : y_offset + h, x_offset : x_offset + w] = img

            name, _ = os.path.splitext(filename)
            new_filename = f"{name}_{max_width}x{max_height}.png"
            cv2.imwrite(os.path.join(path, new_filename), new_img)

    def as_images(
        self,
        dict_of_parts: Dict[str, str],
        reference: str = "../../parts",
    ) -> List[str]:
        return README.Items(
            [
                {
                    "name": self._db[part_name].info[0],
                    "marquee": (self._db[part_name].images + [""])[0],
                    "description": description,
                    "url": f"{reference}/{part_name}.md",
                }
                for part_name, description in dict_of_parts.items()
            ],
            sort=True,
        )

    def as_list(
        self,
        dict_of_parts: Dict[str, str],
        reference: str = "../../parts",
    ) -> List[str]:
        logger.info(
            "{}.subset: {}".format(
                self.__class__.__name__,
                ", ".join(dict_of_parts.keys()),
            )
        )

        for part_name in dict_of_parts:
            if part_name not in self._db:
                logger.error(f"{part_name}: part not found.")
                assert False

        return sorted(
            [
                (
                    "1. [{}{}]({}).".format(
                        self._db[part_name].info[0],
                        ": {}".format(description) if description else "",
                        f"{reference}/{part_name}.md",
                    )
                )
                for part_name, description in dict_of_parts.items()
            ]
        )

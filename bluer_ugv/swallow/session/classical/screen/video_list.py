from typing import Dict, List

from bluer_options.logger.config import log_dict, log_list
from bluer_objects.metadata import get_from_object
from bluer_objects import storage, objects
from bluer_objects.storage.policies import DownloadPolicy

from bluer_ugv.logger import logger


class VideoList:
    def __init__(
        self,
        object_name: str,
    ):
        self.index: int = -1

        self.object_name = object_name
        storage.download(
            self.object_name,
            policy=DownloadPolicy.DOESNT_EXIST,
        )

        self.messages: Dict[str, str] = get_from_object(
            self.object_name,
            "messages",
            default={},
        )
        log_dict(
            logger,
            "messages",
            self.messages,
            "message(s)",
            max_count=-1,
            max_length=-1,
        )

        self.play_list: List[str] = get_from_object(
            self.object_name,
            "play_list",
            default=[],
        )
        log_list(
            logger,
            "messages",
            self.play_list,
            "playlist item(s)",
            max_count=-1,
            max_length=-1,
        )

        logger.info(
            "{} created from {}.".format(
                self.__class__.__name__,
                object_name,
            )
        )

    def get(
        self,
        keyword: int | str,
        what: str = "filename",
    ) -> str:
        filename = f"{keyword.__class__.__name__}-not-supported"

        if isinstance(keyword, int):
            filename = (
                self.play_list[keyword].get(
                    what,
                    f"{what}-not-found",
                )
                if keyword >= 0 and keyword < len(self.play_list)
                else "bad-index-{}-from-{}".format(
                    keyword,
                    len(self.play_list),
                )
            )

        if isinstance(keyword, str):
            filename = (
                self.messages[keyword].get(
                    what,
                    f"{what}-not-found",
                )
                if keyword in self.messages
                else f"{keyword}-not-found"
            )

        return objects.path_of(
            filename=filename,
            object_name=self.object_name,
        )

    def next(self):
        self.index += 1
        if self.index >= len(self.play_list):
            self.index = 0

        logger.info(
            "{}: video #{}".format(
                self.__class__.__name__,
                self.index,
            )
        )

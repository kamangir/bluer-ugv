from typing import Dict, List

from bluer_options.logger.config import log_dict, log_list
from bluer_objects.metadata import get_from_object

from bluer_ugv.logger import logger


class VideoList:
    def __init__(
        self,
        object_name: str,
    ):
        self.messages: Dict[str, str] = get_from_object(
            object_name,
            "messages",
            download=True,
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
            object_name,
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

    def get(self, keyword: int | str) -> str:
        if isinstance(keyword, int):
            return (
                self.play_list[keyword]
                if keyword >= 0 and keyword < len(self.play_list)
                else "bad-index-{}-from-{}".format(
                    keyword,
                    len(self.play_list),
                )
            )

        if isinstance(keyword, str):
            return self.messages.get(
                keyword,
                f"{keyword}-not-found",
            )

        return None

from typing import List, Union
import copy

from bluer_objects import markdown


class Part:
    def __init__(
        self,
        info: Union[List[str], str] = [],
        name: str = "",
        images: List[str] = [],
    ):
        self.name = name

        self.info = (
            copy.deepcopy(info)
            if isinstance(
                info,
                list,
            )
            else [info]
        )

        self.images = (
            copy.deepcopy(images)
            if isinstance(
                images,
                list,
            )
            else [images]
        )

    @property
    def filename(self) -> str:
        return f"docs/parts/{self.name}.md"

    @property
    def README(self) -> List[str]:
        return [f"- {info}" for info in self.info] + (
            [""]
            + markdown.generate_table(
                [f"![image]({image})" for image in self.images],
                cols=3,
            )
            if self.images
            else []
        )

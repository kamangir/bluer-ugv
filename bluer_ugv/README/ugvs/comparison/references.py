from typing import List


class UGV_Reference:
    def __init__(
        self,
        title: str,
        url: str,
        list_of_ugvs: List[str],
    ):
        self.title = title
        self.url = url
        self.list_of_ugvs = list_of_ugvs

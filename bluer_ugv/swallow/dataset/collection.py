from typing import List
from tqdm import tqdm

from blueness import module
from bluer_options.logger import log_list
from bluer_objects import storage
from bluer_objects.metadata import get_from_object
from bluer_objects.storage.policies import DownloadPolicy

from bluer_ugv import NAME
from bluer_ugv import env
from bluer_ugv.logger import logger

NAME = module.name(__file__, NAME)


def collect(
    object_name: str,
    count: int = -1,
    download: bool = True,
) -> bool:
    logger.info(
        "{}.collect({}{}) -> {}".format(
            NAME,
            "all" if count == -1 else f"count={count}",
            ",download" if download else "",
            object_name,
        )
    )

    list_of_datasets: List[str] = get_from_object(
        object_name=env.BLUER_UGV_SWALLOW_DATASET_LIST,
        key="dataset-list",
        default=[],
        download=download,
    )
    if count != -1:
        list_of_datasets = list_of_datasets[-count:]
    log_list(
        logger,
        "collecting",
        list_of_datasets,
        "dataset(s)",
        itemize=True,
    )

    if download:
        for dataset_object_name in tqdm(list_of_datasets):
            logger.info(f"downloading {dataset_object_name} ...")
            if not storage.download(
                dataset_object_name,
                policy=DownloadPolicy.DOESNT_EXIST,
            ):
                return False

    logger.info("🪄")

    return True

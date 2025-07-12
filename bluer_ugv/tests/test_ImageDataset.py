import pytest

from bluer_objects import storage

from bluer_ugv.swallow.dataset.dataset import ImageDataset


@pytest.mark.parametrize(
    ["object_name"],
    [
        ["2025-07-09-10-59-15-x9eemj"],
    ],
)
def test_ImageDataset(object_name: str):
    assert storage.download(object_name=object_name)

    success, dataset = ImageDataset.load(object_name=object_name)
    assert success
    assert isinstance(dataset, ImageDataset)

    assert dataset.generate_timeline()

    assert dataset.save()

import pytest

from bluer_ugv.README.arzhang.validations.db import validations


@pytest.mark.parametrize(
    ["validation_name"],
    [[validation_name] for validation_name in validations],
)
def test_arzhang_validations(validation_name):
    validation_info = validations[validation_name]

    assert "ugv_name" in validation_info, validation_name

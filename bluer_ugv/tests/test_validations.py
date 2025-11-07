import pytest

from bluer_ugv.README.validations.db import dict_of_validations


@pytest.mark.parametrize(
    ["validation_name"],
    [[validation_name] for validation_name in dict_of_validations],
)
def test_arzhang_validations(validation_name):
    validation_info = dict_of_validations[validation_name]

    assert "ugv_name" in validation_info, validation_name

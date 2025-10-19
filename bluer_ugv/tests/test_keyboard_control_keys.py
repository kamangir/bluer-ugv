import pytest

from bluer_ugv.swallow.session.classical.keyboard.keys import ControlKeys


@pytest.mark.parametrize(
    [
        "is_full",
    ],
    [
        [True],
        [False],
    ],
)
def test_keyboard_control_keys(is_full: bool):
    keys = ControlKeys()

    if is_full:
        keys.is_full()

    # ---

    for key, event in keys.special_keys.items():
        assert isinstance(key, str)
        assert len(key) == 1

        assert isinstance(event, str)

    all_special_keys = list(keys.special_keys.keys())
    assert len(all_special_keys) == len(set(all_special_keys)), "repeated special key"

    # ---

    for (
        keyword,
        tuple_of_keys,
    ) in keys._keys.items():  # pylint: disable=protected-access
        assert isinstance(keyword, str)

        assert isinstance(tuple_of_keys, tuple)
        assert len(tuple_of_keys) == 2
        for key in tuple_of_keys:
            assert isinstance(key, str)
            assert len(key) == 1

    # ---

    all_keys = [
        tuple_of_keys[int(keys.is_numpad)]
        for tuple_of_keys in keys._keys.values()  # pylint: disable=protected-access
    ]
    assert len(all_keys) == len(set(all_keys)), "repeated key"


def test_keyboard_control_keys_as_table():
    table = ControlKeys.as_table()

    assert isinstance(table, list)
    for line in table:
        assert isinstance(line, str)

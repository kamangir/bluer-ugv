import pytest

from bluer_ugv.README.ugvs.get import get


@pytest.mark.parametrize(
    [
        "ugv_name",
        "what",
        "expected_output",
    ],
    [
        [
            "azarakhsh",
            "tagline",
            "not-found",
        ],
        [
            "swallow",
            "tagline",
            "the first one.",
        ],
        [
            "swallow",
            "computers.radar",
            "not-found",
        ],
        [
            "swallow",
            "computers.front",
            "swallow2",
        ],
        [
            "swallow",
            "computers.front",
            "swallow2",
        ],
    ],
)
def test_ugvs_get(
    ugv_name: str,
    what: str,
    expected_output: str,
):
    assert (
        get(
            ugv_name,
            what,
        )
        == expected_output
    )

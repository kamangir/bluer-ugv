import pytest

from bluer_ugv.README.ugvs.get import get


@pytest.mark.parametrize(
    [
        "ugv_name",
        "what",
        "include_comments",
        "expected_output",
    ],
    [
        [
            "azarakhsh",
            "tagline",
            False,
            "not-found",
        ],
        [
            "swallow",
            "tagline",
            True,
            "the first one.",
        ],
        [
            "swallow",
            "computers.radar",
            False,
            "not-found",
        ],
        [
            "swallow",
            "computers.front",
            False,
            "swallow2",
        ],
        [
            "swallow",
            "computers.front",
            True,
            "swallow2 (`swallow` was used for Ubuntu experiments)",
        ],
    ],
)
def test_ugvs_get(
    ugv_name: str,
    what: str,
    include_comments: bool,
    expected_output: str,
):
    assert (
        get(
            ugv_name,
            what,
            include_comments,
        )
        == expected_output
    )

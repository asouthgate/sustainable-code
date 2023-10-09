import pyunsustainable.find_tokens_refactored as ft


# We could use pytest.parameterize(...
def test_alignment_distance():
    assert ft.alignment_distance("oranges", "oranges") == 0
    assert ft.alignment_distance("sand", "land") == 1
    assert ft.alignment_distance("and", "land") == 1
    assert ft.alignment_distance("lan", "land") == 1
    assert ft.alignment_distance("", "land") == 4

    # How else could we test this?
    # ...


def test_something_fails():
    """This test will fail and prevent the pre-commit hook from returning 0"""
    assert False

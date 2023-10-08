import pyunsustainable.find_tokens as ft


# We could use pytest.parameterize(...
def test_edit_distance():
    # The edit distance between 2 strings that are the same should be 0
    assert ft.edit_distance("oranges", "oranges") == 0
    assert ft.edit_distance("sand", "land") == 1
    assert ft.edit_distance("and", "land") == 1
    assert ft.edit_distance("lan", "land") == 1
    assert ft.edit_distance("", "land") == 4

    # How else could we test this?
    # ...


def test_something_fails():
    """This test will fail and prevent the pre-commit hook from returning 0"""
    assert False

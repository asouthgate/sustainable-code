from pyunsustainable import find_tokens


def test_filter_words_empty_intersection():
    """Test that words with no characters from the alphabet are filtered out."""
    alphabet = set("abc")
    words = ["hello", "world"]
    filtered_words = find_tokens.filter_words(words, alphabet, 0.0)
    raise NotImplementedError


def test_always_fail():
    """This test will fail and prevent the pre-commit hook from returning 0"""
    assert False

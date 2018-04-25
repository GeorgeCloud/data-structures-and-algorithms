from multi_bracket_validation import multi_bracket_validation
import pytest


def test_multi_bracket_validation_empty():
    """Validate empty string returns True."""
    assert multi_bracket_validation('') is True


def test_multi_bracket_validation_single():
    """Validate for one bracket that valuates to False."""
    assert multi_bracket_validation('[') is False


def test_multi_bracket_validation_evenly():
    """Validate single pair returns True."""
    assert multi_bracket_validation('[]') is True


def test_multi_bracket_validation_words_and_brackets():
    """Validate words dont affect bracket pattern search."""
    assert multi_bracket_validation('hello[]world') is True


def test_multi_bracket_validation_uneven():
    """Validate unven brackets returns False."""
    assert multi_bracket_validation('][({}){}]') is False

from multi_bracket_validation import multi_bracket_validation
import pytest

def test_multi_bracket_validation_empty():
    assert multi_bracket_validation('') is True

def test_multi_bracket_validation_single():
    assert multi_bracket_validation('[') is False

def test_multi_bracket_validation_evenly():
    assert multi_bracket_validation('[]') is True

def test_multi_bracket_validation_evenly():
    assert multi_bracket_validation('hello[]world') is True

def test_multi_bracket_validation_uneven():
    assert multi_bracket_validation('][({}){}]') is False

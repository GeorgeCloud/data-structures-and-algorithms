from hash_table import HashTable
from repeated_word import repeated_word
import pytest


@pytest.fixture
def min_string():
    return "Huge things are complied of smaller things. Essentilly everything is made of smaller works of art."


@pytest.fixture
def multiple_occurrences_string():
    string = "Some times I Idecide to walk around the house and contemplate about things in my past life. Other days I stay home and do nothing"
    return string


@pytest.fixture
def no_occurrences_string():
    string = "Video games seem to change my mood rather quickly depending on the type of game."
    return string


def test_empty_string():
    """Checks if empty string returns false."""
    assert repeated_word("") is False


def test_no_match_string(no_occurrences_string):
    """Test against special charcters"""
    assert repeated_word(no_occurrences_string) is False


def test_minimum_string(min_string):
    """test small string"""
    assert repeated_word(min_string) == "of"


def test_mult_string(multiple_occurrences_string):
    """Return first occurrence in larger string set"""
    assert repeated_word(multiple_occurrences_string) == "other"


def test_new_string():
    """Test against special charcters"""
    assert repeated_word("hello!! world!! how!! are!! you!!HELLO??") is False

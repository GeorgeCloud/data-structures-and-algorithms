from mergesort import mergesort
import pytest


@pytest.fixture
def unordered_array():
    small_array = [23, 4, 93, 45, 78, 4, 23, 9, 8, 7, 4, 25]
    return small_array


@pytest.fixture
def small_array():
    small_array = [7, 56, 10]
    return small_array


def test_super_small():
    """Sorts with an edge case of one element inside array."""
    assert mergesort([7]) == [7]


def test_small_array(small_array):
    """Validates"""
    assert mergesort(small_array) == sorted(small_array)


def test_big_array(unordered_array):
    """test big array"""
    assert mergesort(unordered_array) == sorted(unordered_array)

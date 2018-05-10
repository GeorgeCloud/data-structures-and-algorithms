from radix_sort import radixSort
import pytest


@pytest.fixture
def invalid_array():
    return ['invalid', 'random', 3, 'values', 4]


@pytest.fixture
def unsorted_array():
    return [6, 3, 8, 3, 8, 23, 7, 3, 1, 6, 23, 13]


@pytest.fixture
def sorted_array():
    return [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def test_invalid_data(invalid_array):
    """Validates that the type inputed returns a type error"""
    with pytest.raises(TypeError):
        radixSort(invalid_array)


def test_returns_sorted_array(unsorted_array):
    """Sorts an unordered array with random values."""
    assert radixSort(unsorted_array) == sorted(unsorted_array)


def test_returns_already_sorted(sorted_array):
    """Sorts an already sorted array."""
    assert radixSort(sorted_array) == sorted(sorted_array)

from quicksort import quickSort
import pytest


@pytest.fixture
def invalid_array():
    return ['invalid', 4, 'datatypes', 5, 6, 'helloworld']


@pytest.fixture
def almost_sorted_array():
    return [1, 4, 7, 2, 8, 9, 10]


@pytest.fixture
def unsorted_array():
    return [9, 9, 0, 2, 13, 47, 1, 89, 0, 4, 3]


@pytest.fixture
def sorted_array():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_invalid_input(invalid_array):
    """Validates taht array given is return an error for wrong input datatype."""
    with pytest.raises(TypeError):
        quickSort(invalid_array)


def test_almost_sorted(almost_sorted_array):
    """Ensures quicksort can return a sorted array with almost sorted input."""
    assert quickSort(almost_sorted_array) == sorted(almost_sorted_array)


def test_sorts_unordered_array(unsorted_array):
    """Validates that quicksort returns fully sorted array in any random order."""
    assert quickSort(unsorted_array) == sorted(unsorted_array)


def test_returns_already_sorted_array(sorted_array):
    """Validaes that quicksort returns an already sorted array."""
    assert quickSort(sorted_array) == sorted(sorted_array)

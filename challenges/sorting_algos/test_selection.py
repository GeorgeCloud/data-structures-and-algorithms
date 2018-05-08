from selection import selectionSort
import pytest


@pytest.fixture
def unsorted_arr():
    return [5, 3, 4, 2, 0, 13, 4, 8, 0, 92, 31, 46, 7, 82, 14]


@pytest.fixture
def many_non_unique_arr():
    return [2, 2, 2, 2, 2, 1, 2, 2, 2, 5, 2, 2, 2, 2]


@pytest.fixture
def only_unique_arr():
    return [35, 23, 10, 2, 234, 634, 234234, 12, 1, 6, 49]


def test_invalid_input():
    """Validates that input requires array type."""
    with pytest.raises(TypeError):
        selectionSort(234)


def test_selection_sort(unsorted_arr):
    assert selectionSort(unsorted_arr) == sorted(unsorted_arr)


def test_almost_non_unique_array(many_non_unique_arr):
    assert selectionSort(many_non_unique_arr) == sorted(many_non_unique_arr)


def test_unique_array(only_unique_arr):
    assert selectionSort(only_unique_arr) == sorted(only_unique_arr)

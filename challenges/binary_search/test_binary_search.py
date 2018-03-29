from binary_search import binary_search

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_binary_search_empty_list():
    """Validates if array is empty"""
    assert binary_search([], 5) == -1


def test_binary_search_returns_index():
    """Validates if value given returns the correct index of value in array."""
    assert binary_search(arr, 7) == 6


def test_binary_search_no_found():
    """Returns -1 if the value was not found, uses a binary search"""
    assert binary_search([], 2) == -1

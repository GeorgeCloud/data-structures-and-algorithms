from binary_search import binarySearch
import pytest


def test_binary_search_empty_list():
    """Returns negative one if an array is empty as a first parameter"""
    assert binarySearch([], 2) == -1


def test_binary_search_returns_index():
    """Returns index if exists"""
    assert binarySearch([1, 2, 3, 4, 5, 6], 6) == 5


def test_binary_search_returns_first_occurrence():
    """Returns first occurrence and the index"""
    assert binarySearch([0, 1, 0, 1, 2, 3, 3], 3) == 5


def test_binary_search_no_found():
    """Returns negative 1 if element is not found"""
    assert binarySearch([1, 2, 3, 4, 5, 6], 40000) == -1

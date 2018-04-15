from binary_search import binarySearch
import pytest, time

def test_binary_search_empty_list():
	assert binarySearch([], 2) == -1

def test_binary_search_returns_index():
	assert binarySearch([1, 2, 3, 4, 5, 6], 4) == 3

def test_binary_search_no_found():
	assert binarySearch([1, 2, 3, 4, 5, 6], 40000) == -1

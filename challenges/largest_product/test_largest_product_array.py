import pytest
from largest_product_array import largest_product


def test_empty_product_arr():
    """Validating zero is returned if no number is entered"""
    assert largest_product([]) == 0


def test_largest_product_array():
    """Validating product of 7 & 8 is the highest return"""
    assert largest_product([[1, 2], [3, 4], [5, 6], [7, 8]]) == 56


def test_largest_product_2_arrays():
    """Validating two arrays inside matrix"""
    assert largest_product([[1, 2], [3, 4]]) == 12


def test_largest_product_one_array():
    """Validating one array inside matrix"""
    assert largest_product([[1, 2]]) == 2


def test_largest_product_negative():
    """Validating negative numbers don't change value."""
    assert largest_product([[-1, -2], [-3, -4], [-5, -6], [-7, -8]]) == 56

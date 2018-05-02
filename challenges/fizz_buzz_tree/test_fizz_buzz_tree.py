import pytest
from bst import BST
from fizz_buzz_tree import fizzbuzztree


@pytest.fixture
def empty_bst():
    """make empty bst"""
    return BST()


@pytest.fixture
def small_bst():
    return BST([4, 3, 3.5, 2, 5, 6, 7])


@pytest.fixture
def min_bst():
    return BST([3, 5, 15, 45])


def test_inorder_traverse(small_bst):
    a = []
    new_tree = fizzbuzztree(small_bst)
    new_tree.in_order(a.append)
    assert a == [2, "Fizz", 3.5, 4, "Buzz", 'Fizz', 7]


def test_post_order_(empty_bst):
    assert fizzbuzztree(empty_bst) is False


def test_post_order(min_bst):
    a = []
    new_tree = fizzbuzztree(min_bst)
    new_tree.in_order(a.append)
    assert a == ['Fizz', 'Buzz', 'FizzBuzz', 'FizzBuzz']

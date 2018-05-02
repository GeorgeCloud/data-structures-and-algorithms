import pytest
from .bst import BST


@pytest.fixture
def small_bst():
    return BST([26, 25, 7, 8, 6, 24, 2])


@pytest.fixture
def empty_bst():
    return BST()

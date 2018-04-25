from .k_tree import KTree
import pytest


@pytest.fixture
def one_element_tree():
    return KTree(1)


@pytest.fixture
def numerous_childs():
    k_tree = KTree(1)
    k_tree.insert(2, 1)
    k_tree.insert(3, 2)
    k_tree.insert(4, 3)
    return k_tree


def test_empty_k_tree(new_k_tree):
    pass


def test_level_order_no_childs(numerous_childs):
    pass

from tree_intersection import tree_intersection
from bst import BST
# import pytest


unique_tree = BST([8345, 9345, 124, 435])
tree1 = BST([1, 1, 1, 2])
tree2 = BST([5, 6, 7, 1])
empty_tree = BST([])


def test_empty_and_full_tree():
    """Validing that an empty and a filled tree return no common vals."""
    assert tree_intersection(tree1, empty_tree) == []


def test_trees_intersect_vals():
    """Checking for a tree with one common val."""
    assert tree_intersection(tree1, tree2) == [1]


def test_multiple_trees_common_values():
    """"Test multiple values are found inside both."""
    assert tree_intersection(tree2, BST([7, 6, 5, 4, 1])) == [1, 5, 6, 7]


def test_no_values_in_common():
    """Validate that no values are common between two bst trees with intersections."""
    assert tree_intersection(tree2, unique_tree) == []

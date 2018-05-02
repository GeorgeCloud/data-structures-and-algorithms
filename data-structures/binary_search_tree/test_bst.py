# import pytest


def test_tree_empty_instance(empty_bst):
    """Check if root of binary tree is None"""
    assert empty_bst.root is None


def test_insert_empty(empty_bst):
    """Check Binary tree root"""
    empty_bst.insert('some random value')
    assert empty_bst.root.val == 'some random value'


def test_repr_small_bst(small_bst):
    """Test newly created binary tree"""
    assert small_bst.root.val == 26
    assert small_bst.root.left.val == 25


def test_inorder_traverse(small_bst):
    """test if in order is sorting by value"""
    collection = []
    small_bst.in_order(collection.append)
    # You can assume 'collection' has all the values by line 31
    assert collection == [2, 6, 7, 8, 24, 25, 26]


def test_pre_order(small_bst):
    """
    Test Preorder traversal: traverses from top to left to right without
    order
    """
    collection = []
    small_bst.pre_order(collection.append)
    assert collection == [26, 25, 7, 6, 2, 8, 24]


def test_post_order(small_bst):
    """
    Test postorder traversal: Traverses tree from bottom left to right most
    """
    collection = []
    small_bst.post_order(collection.append)
    assert collection == [2, 6, 24, 8, 7, 25, 26]

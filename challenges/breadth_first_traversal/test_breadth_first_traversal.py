

from bst import BST
import pytest
from breadth_first_traversal import breadthFirstTraversal as bft


def test_incorrect_bst_breadthFirstTraversal():
    """invalid arguments Passed into breadthFirstTraversal"""
    with pytest.raises(TypeError):
        assert bft(4)

def test_breadthFirstTraversal_root():
    tree = BST([5])
    assert len(bft(b)) == 5
    assert bft(b)[0].val == 5

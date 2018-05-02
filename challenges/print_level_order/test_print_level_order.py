from print_level_order import print_level_order
from k_tree import KTree, Node
import pytest


@pytest.fixture
def small_k_tree():
    """small tree creation."""
    tree = KTree('string1')
    tree.root.children = [Node(i) for i in ['string2', 'string3', 'string4']]
    return tree


@pytest.fixture
def mid_k_tree():
    tree = KTree('string1')
    tree.root.children = [Node(i) for i in ['string2', 'string3', 'string4']]
    tree.root.children["string1"].children = [Node(21), Node(22)]
    tree.root.children[1].children = [Node(3)]
    tree.root.children[2].children = [Node(i) for i in ['a1, b1, c1, d1']]
    tree.root.children[2].children[3].children = [Node('2'), Node('1')]
    return tree


def test_invalid_argument():
    """Testing with invalid args."""
    with pytest.raises(TypeError):
        assert print_level_order('sdffs')


def test_small_tree(small_k_tree):
    '''Testing regular tree for join.'''
    expected = ["string1", "string2 string3 string4"]
    assert '\n'.join(expected) == print_level_order(small_k_tree)

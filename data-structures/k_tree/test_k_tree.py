from .k_tree import KTree, Node
import pytest


@pytest.fixture
def small_tree():
    tree = KTree('languages')
    tree.root.children = [Node(i) for i in ['Python', 'C', 'Java', 'Go']]
    return tree


@pytest.fixture
def tree():
    tree = KTree("STARTING")
    tree.root.children = [Node(i) for i in ["browne", "white", "kenzo"]]
    tree.root.children[0].children = [Node("oceanblue"), Node("lemon")]
    tree.root.children[1].children = [Node("timeless")]
    tree.root.children[2].children = [Node(i) for i in ["bolt", "water", "laurent", "count"]]
    tree.root.children[2].children[3].children = [Node("soundcolor"), Node("altj")]
    return tree


def test_node_str():
    """Validate node print string."""
    node = Node('somenodeval')
    assert node.__str__() == 'somenodeval'


def test_node_repr():
    """Testing node representation prints correct root value"""
    node = Node('ZARA')
    assert node.__repr__() == 'Instance of Node with value of {}.'.format(node.val)


def test_tree_repr(small_tree):
    """Validate tree representation."""
    assert small_tree.__repr__() == 'Instance of K-ary Tree. Root: {}.'.format('languages')


def test_tree_str(small_tree):
    """Validate tree print string."""
    assert small_tree.__str__() == 'languages, Python, C, Java, Go'


def test_pre_order_small(small_tree):
    """Validate preorder traverse on small tree."""
    test_string = 'languages, Python, C, Java, Go'
    s = []
    small_tree.pre_order(lambda n: s.append(str(n.val)))
    assert ', '.join(s) == test_string


def test_bad_traversal_parameter(small_tree):
    """Validate incorrect parameters into traversal."""
    with pytest.raises(TypeError):
        assert small_tree.pre_order('water')
        assert small_tree.post_order('blue')
        assert small_tree.breadth_first_traversal('breeze-blocks')


def test_pre_order_mid(tree):
    """Validate preorder traversal."""
    test_string = "STARTING, browne, oceanblue, lemon, white, timeless, kenzo, bolt, water, laurent, count, soundcolor, altj"
    s = []
    tree.pre_order(lambda n: s.append(str(n.val)))
    assert ', '.join(s) == test_string


def test_post_order_small(small_tree):
    """Validate postorder traversal on smaller tree."""
    test_string = "Python, C, Java, Go, languages"
    s = []
    small_tree.post_order(lambda n: s.append(str(n.val)))
    assert ', '.join(s) == test_string


def test_post_order_mid(tree):
    """Validate postorder on tree."""
    test_string = "oceanblue, lemon, browne, timeless, white, bolt, water, laurent, soundcolor, altj, count, kenzo, STARTING"
    s = []
    tree.post_order(lambda n: s.append(str(n.val)))
    assert ', '.join(s) == test_string


def test_breadth_first(tree):
    """Validate Breadthfirst traversal."""
    test_string = "STARTING, browne, white, kenzo, oceanblue, lemon, timeless, bolt, water, laurent, count, soundcolor, altj"
    s = []
    tree.breadth_first_traversal(lambda n: s.append(str(n.val)))
    assert ', '.join(s) == test_string

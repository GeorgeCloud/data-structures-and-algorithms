from bst import BST
from find_maximum_value_binary_tree import findMaxValue


def test():
    assert 1 == 1


def tests_empty_bst():
    """Tests if bst is empty with no elements"""
    empty = BST()
    assert findMaxValue(empty) is None


def test_bst_with_numerous_numbers():
    """Test findMaxValue against multiple numbers"""
    c = BST([4, 3, 2, 1, 8, 6, 12, 9])
    assert findMaxValue(c) == 12


def test_left_bst_breadth_first():
    """Tests against negative numbers"""
    ll = BST([-2, -7, -1, -3, -4])
    assert findMaxValue(ll) == -1


def test_find_max_filter_elements():
    """Filters elements to numbers only and find max value"""
    check = BST([7, 7, 'other item', 7, 8, 'elements', 2, 2, 2, 'help'])
    assert findMaxValue(check) == 8


def test_bst_with_all_types():
    """Tests findMaxValue against negative and postitives and strings"""
    c = BST([4, 'lana', 2, 1, 'del', -8, 6, 'rey', 12, -9])
    assert findMaxValue(c) == 12

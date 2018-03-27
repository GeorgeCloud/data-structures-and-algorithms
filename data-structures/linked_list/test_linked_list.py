from linked_list import LinkedList
from node import Node
# import pytest


def test_linked_list_creation():
    """Validating if Linked List was Created."""
    ll = LinkedList([2, 3, 4, 5])
    assert Node(2).val is ll.head.val
    assert isinstance(ll.head.val, int)


def test_insert_into_linkedlist():
    """Validating if the value inserted into a Linked-List was the same as\
    inputed inside a Node object."""
    ll = LinkedList()
    assert (4 is not ll.head)
    ll.insert(4)
    assert True == (Node(4).val == ll.head.val)


def test_find_value():
    """Validates if value was found by find function."""
    books = LinkedList(['Python The Hard Way', 'The Pragmatic Programmer', 'The\
    Hunger Games', 'Mr. Robot'])
    books.insert(4)
    assert 4 is books.head.val
    assert True is books.find('The Pragmatic Programmer')


def test_current_node_value():
    """Checking for attributes inside __init__"""
    node = Node([1, 2, 3, 4, 5])
    assert isinstance(node.val, list)


def test_append():
    ll = LinkedList(['book one', 'book two'])
    ll.append('a')
    assert ll.find('a')
    assert 'a' == ll.head._next._next.val


def test_insert_before():
    ll = LinkedList(['a', 'b', 'c'])
    ll.insert_before('a', 'z')
    assert 'a' == ll.head.val
    assert isinstance(ll.head.val, str)


def test_insert_after():
    ll = LinkedList(['a', 'b', 'c'])
    ll.insert_after('a', 'z')
    assert 'z' == ll.head._next.val

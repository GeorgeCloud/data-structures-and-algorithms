from linked_list import LinkedList
from node import Node
import pytest


def test_linked_list_creation():
    """Validating if Linked List was Created."""
    ll = LinkedList([2, 3, 4, 5])
    assert Node(2).val is ll.head.val


def test_insert_into_linkedlist():
    """Validating if the value inserted into a Linked-List was the same as inputed inside a Node object."""
    ll = LinkedList()
    ll.insert(4)
    assert Node(4).val == ll.head.val

def test_find_value():
    """Validates if value was found by find function."""
    books = LinkedList(['Python The Hard Way', 'The Pragmatic Programmer',
        'The Hunger Games', 'Mr. Robot'])

    assert True is books.find('The Pragmatic Programmer')


def test_current_node_value():
    """Checking for attributes inside __init__"""
    node = Node([1, 2, 3, 4, 5])
    assert type(node.val) == type([10])

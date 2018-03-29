from linked_list import LinkedList
from node import Node
from mergeList import ll_merge
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
    assert ll.find('a') is True
    assert 'a' == ll.head._next.val


def test_insert_before():
    ll = LinkedList(['a', 'b', 'c'])
    ll.insert_before('a', 'z')
    assert 'z' == ll.head.val
    assert ll.find('z') is True


def test_insert_after():
    ll = LinkedList(['a', 'b', 'c'])
    ll.insert_after('a', 'z')
    assert 'z' == ll.head._next.val


def test_kkthFromEnd():
    """
    Checks if the linked-list is empty
    Checks if out of range in Linked-List
    Returns node with correct key value
    """
    nodes1 = LinkedList(['a', 1, 'hello world', 5.0, True])
    assert nodes1.kthFromEnd(3) == 1

    nodes2 = LinkedList([])
    assert nodes2.kthFromEnd(5) == 'LinkedList is empty.'
    nodes2.insert([5, 6, 7, 8, 9, 10])
    assert nodes2.kthFromEnd(100) is False


def test_ll_merge():
    """
    Validates if LinkedList is empty.
    Returns Correct head node of LinkedList.
    Returns the whole LinkedList merged.
    """
    arr1 = LinkedList()
    arr2 = LinkedList()
    LL = ll_merge(arr1, arr2)
    assert LL is False

    # Adding 6 to LinkedList
    arr1 = LinkedList([6])
    LL = ll_merge(arr1, arr2)
    assert LL.head.val == 6

    # Combining TWO LinkedList
    arr1 = LinkedList([1, 3, 5, 7])
    arr2 = LinkedList([2, 4, 6, 8])
    LL = ll_merge(arr1, arr2)
    assert LL.head.val.val == 1
    assert LL.head._next.val == 2
    assert LL.head._next._next.val.val == 3
    assert LL.head._next._next._next.val == 4

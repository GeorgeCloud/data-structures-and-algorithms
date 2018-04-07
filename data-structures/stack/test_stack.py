from stack import Stack
import pytest


new_stack = Stack()


def test_empty():
    assert new_stack.head is None


def test_stack_pop():
    ll = Stack([6])
    assert ll.pop() == 6
    ll.push(8)
    assert ll.pop() == 8

def test_stack_pop_error():
    while new_stack._size:
        new_stack.pop()
    assert new_stack._size == 0
    with pytest.raises(IndexError):
        new_stack.pop()


def test_stack_size():
    assert new_stack._size == 0
    new_stack.push('learn faster')
    assert new_stack._size == 1


def test_stack_push():
    new_stack.push(5)
    assert new_stack.head.val == 5


def test_stack_size_increase():
    assert new_stack._size == 2
    new_stack.pop()
    new_stack.pop()
    assert new_stack._size == 0


def test_peek():
    new_stack.push('books')
    assert new_stack.peek() == 'books'

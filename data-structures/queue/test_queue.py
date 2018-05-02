from queue import Queue
import pytest

new_queue = Queue()


def test_size():
    """Validating if the size is increaseing with queues"""
    assert new_queue._size == 0
    new_queue.enqueue('emma')
    assert new_queue._size == 1


def test_enqueue():
    """Validing if the appended value was added to the back of the Queue"""
    new_queue.enqueue('jim')
    assert new_queue.head.val == 'jim'
    new_queue.head._next.val == 'emma'


def test_dequque_before():
    """Removing the front node of the Queue"""
    assert new_queue.dequeue() == 'emma'
    assert new_queue._size == 1

def test_dequque_after():
    """Validating if front node was removed and didn't have the same value"""
    assert new_queue.dequeue() != 'emma'
    assert new_queue._size == 0

def test_dequque_error():
    nq = Queue()
    with pytest.raises(IndexError):
        nq.dequeue()

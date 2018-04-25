from queue_with_stack import Queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    return Queue(['7', '4', 4])


# Length check
def test_constractor(empty_queue):
    """test queue size before methods"""
    assert empty_queue._len == 0


def test_dequeue_error(empty_queue):
    """test Dequeue when no items are inside Queue"""
    assert empty_queue.dequeue() is False


# Dequeue Tests
def test_dequeue(small_queue):
    """Test Queue using stack"""
    assert small_queue.dequeue() == '7'


def test_enqueue_and_dequeue(empty_queue):
    """Enqueue and dequeue after"""
    empty_queue.enqueue('z')
    assert empty_queue.dequeue() == 'z'


# Test Enqueue Method
def test_enqueue_nums(empty_queue):
    """Check Enqueue and with empty queue"""
    assert empty_queue.enqueue(1) == empty_queue.stack1
    assert empty_queue.dequeue() == 1


def test_enquueue():
    """Test new queue with single node"""
    new_line = Queue(['Tom Browne'])
    assert new_line.dequeue() == 'Tom Browne'

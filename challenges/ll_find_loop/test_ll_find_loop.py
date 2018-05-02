from ll_find_loop import LinkedList

# Constant LinkedList for all tests
LL = LinkedList([1, 3, 6, 3, 9])


def test_ll_find_loop_False():
    """Checks If there is no loop inside LinkedList."""
    assert LL.has_loop() is False


def test_ll_find_loop_insert():
    """Inserts value and check if loop is still false"""
    LL.insert(4)
    assert LL.has_loop() is False


def test_ll_find_loop_true():
    """Checks if the LinkedList looping through node infinitely."""
    LL.head._next._next = LL.head
    assert LL.has_loop() is True


def test_ll_find_loop_2nd_node():
    """Checks 1 node ahead and check if it still loops"""
    LL.head._next = LL.head
    assert LL.has_loop() is True


def test_ll_find_loop_true_3rd_node():
    """Checks 3 nodes ahead and check if it still loops"""
    LL.head._next._next._next = LL.head
    assert LL.has_loop() is True

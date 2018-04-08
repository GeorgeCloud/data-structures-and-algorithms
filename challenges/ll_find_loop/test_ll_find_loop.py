from ll_find_loop import LinkedList


LL = LinkedList([1, 3, 6, 3, 9])


# Checks If there is no loop inside LinkedList.
def test_ll_find_loop_False():
    assert LL.has_loop() is False


def test_ll_find_loop_insert():
    LL.insert(4)
    assert LL.has_loop() is False


# Checks if the LinkedList looping through node infinitely.
def test_ll_find_loop_true():
    LL.head._next._next = LL.head
    assert LL.has_loop() is True


def test_ll_find_loop_2nd_node():
    LL.head._next = LL.head
    assert LL.has_loop() is True


def test_ll_find_loop_true_3rd_node():
    LL.head._next._next._next = LL.head
    assert LL.has_loop() is True

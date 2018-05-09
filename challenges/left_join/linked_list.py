class Node:
    def __init__(self, value, next=None):
        self.val = value
        self._next = next


class LinkedList:
    def __init__(self, iter=()):
        self.head = None
        self._len = 0
        for value in reversed(iter):
            self.insert(value)

    def insert(self, value):
        self.head = Node(value, self.head)
        self._len += 1

    def remove(self, value):
        if self.head is None:
            raise ValueError('Value not found.')
        if self.head.val == value:
            self.head = self.head._next
            self._len -= 1
            return self.head
        node = self.head
        while node._next is not None:
            if node._next.val == value:
                self.head = self.head._next
                self._len -= 1
                return self.head
            node = node._len
        raise ValueError('remove value not in LinkedList')

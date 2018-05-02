class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


class Queue:
    def __init__(self, iter=()):

        self.head = None
        self._size = 0

        for value in iter:
            self.enqueue(value)

    def __len__(self):
        return self._size

    def dequeue(self):
        if not self.head:
            raise IndexError('')
        node = self.head
        if not node._next:
            self.head = None
            self._size -= 1
            return node.value
        while node._next._next:
            node = node._next
        node._next, node = None, node._next
        self._size -= 1
        return node.value

    def enqueue(self, value):
        self.head = Node(value, self.head)
        self._size += 1

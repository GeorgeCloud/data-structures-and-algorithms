class Node:
    def __init__(self, value, next=None):
        self.val = value
        self._next = next


class Queue:
    def __init__(self, iter=()):
        self.head = None
        self._size = 0
        for el in iter:
            self.enqueue(el)

    def dequeue(self):
        if not self.head:
            raise IndexError('')
        node = self.head
        if not node._next:
            self.head = None
            self._size -= 1
            return node.val
        while node._next._next:
            node = node._next
        node._next, node = None, node._next
        self._size -= 1
        return node.val

    def enqueue(self, value):
        self.head = Node(value, self.head)
        self._size += 1

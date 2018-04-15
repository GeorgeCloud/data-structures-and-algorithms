from node import Node

class Stack:
    def __init__(self, iter=[]):
        self.top = None
        self._size = 0

        for element in iter:
            self.push(element)

    def __str__(self):
        return 'Top: {}'.format(self.top)

    def push(self, val):
        self.top = Node(val, self.top)
        self._size += 1

    def pop(self):
        curr = self.top
        self.top = self.top._next
        self._size -= 1
        return curr

    def peek(self):
        pass

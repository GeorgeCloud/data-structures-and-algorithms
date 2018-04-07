from node import Node

class Queue:
    def __init__(self, iter=()):
        self.head = None
        self._size = 0
        for el in iter:
            self.enqueue(el)

    def __str__(self):
        """Returns string with Queue informations(head, length)"""
        if self.head:
            return 'Stacks First value is {} and length is {}\
            '.format(self.head.val, self._size)
        return 'Stack Empty'

    def __len__(self):
        """Returns size of Queue Instance"""
        return self._size

    def enqueue(self, val):
        """Appends to the end of the line"""
        self.head = Node(val, self.head)
        self._size += 1

    def dequeue(self):
        """Pops front node of Queue and returns it"""
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




# line = Queue(['tom', 'brown', 'kenzo', 'kim'])
# print(line.head)

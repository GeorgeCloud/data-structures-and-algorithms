class Node:
    def __init__(self, value, next=None):
        self.val = value
        self._next = next


class Stack:
    def __init__(self, iter=()):
        self.head = None
        self._size = 0
        for el in iter:
            self.push(el)

    def __str__(self):
        if self.head:
            return 'Stacks Head value is {} and length is {}\
            '.format(self.head.val, self._size)
        return 'Stack Empty'

    def __len__(self):
        return self._size

    def push(self, val):
        self.head = Node(val, self.head)
        self._size += 1

    def pop(self):
        if not self.head:
            raise IndexError('')
        node = self.head
        self.head = self.head._next
        self._size -= 1
        return node.val

    def peek(self):
        """Returns head node"""
        if not self.head:
            raise IndexError('')
        return self.head.val


# pringles = Stack([1,2,3,4])
# pringles.push(3)
#
# print(pringles.head)

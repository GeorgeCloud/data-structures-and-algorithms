class Node:
    def __init__(self, value, next=None):
        self.val = value
        self._next = next

    def _has_loop(self):
        """
        Checks if last element is None or if the LinkedList is infinite.
        Returns Boolean.
        """
        node1 = self
        node2 = node1._next
        while node2:
            if node1 is node2:
                return True
            node2 = node2._next
            if not node2:
                return False
            if node1 is node2:
                return True
            node1 = node1._next
            node2 = node2._next
        return False


class LinkedList:
    def __init__(self, arr=()):
        self.head = None
        self._len = 0
        if arr:
            for element in arr[::-1]:
                self.insert(element)

    def __str__(self):
        return "String Here"

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        current = self.head
        self.head = Node(value)
        self.head._next = current

    def has_loop(self):
        """Returns True if LinkedList is infinite else returns False."""
        if not self.head:
            return False
        return self.head._has_loop()

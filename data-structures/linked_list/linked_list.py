from node import Node


class LinkedList(object):
    """Creates a data structure to link data together by attributes"""
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._len = 0

        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        """Prints a the head pointer of the current Linked-List"""
        return 'Head of Node: {}'.format(self.head.val)

    def __len__(self):
        """Returns LinkedLists Length"""
        return self._len

    def insert(self, val):
        """Inserts new Node into Linked-List and sets it as a head pointer"""
        self.head = Node(val, self.head)
        self._len += 1

    def find(self, value):
        """Finds users input within Linked-List"""
        current = self.head
        while current:
            if value == current.val:
                return True
            else:
                current = current._next
        return False

    def append(self, newVal):
        """appends a value at the end of the linked list."""
        current = self.head
        while current:
            current = current._next
            self.insert(newVal)
            self._len += 1
        return self._len

    def insert_before(self, value, newVal):
        """inserts a node before a specified node value"""
        new_node = Node(newVal)
        if value == self.head.val:
            self.head = Node(newVal, self.head)
        current = self.head
        while current._next is not None:
            if current._next.val == value:
                new_node._next = current._next
                current._next = new_node
                self._len += 1
                return self._len
            current = current._next
        if current.val is None:
            raise ValueError("Data not in list")

    def insert_after(self, value, newVal):
        """inserts a node after a specified node value"""
        current = self.head
        while current is not None:
            if current.val == value:
                self._len += 1
                current._next = Node(newVal, current._next)
            current = current._next


if __name__ == "__main__":
    try:
        ll = LinkedList([1, 2, 3, 4])
        print(ll.kthFromEnd(1))
    except TypeError:
        print("This Linked-List takes one array as a parameter")

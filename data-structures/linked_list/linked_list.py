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

    def remove(self, value):
        pass

    def find_by_index(self, index):
        pass


if __name__ == "__main__":
    try:
        ll = LinkedList([1, 2, 3, 4])
        # print(ll.find(5))
    except TypeError:
        print("This Linked-List takes one array as a parameter")

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self._next = next

    def __repr__(self):
        return "Node val: {}".format(self.val)

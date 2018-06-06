class Node:
    """Simple node structure."""
    def __init__(self, value, next=None):
        self.val = value
        self._next = next


class Queue:
    """Queue Data-structures. Used for minimal space.(Improved Queue)"""
    def __init__(self, iter=()):
        self.head = None
        self.back = None
        self._len = 0
        
        for element in iter:
            self.enqueue(element)
            self._len += 1

def enqueue(self, value):
    """APPENDS element to the back of queue."""
    element = Node(value)
    
    if self.head:
        self.back._next = element
            self.back = self.back._next
        else:
            self.head = element
            self.back = element

def dequeue(self):
    """REMOVES & RETURNS element from the front of the queue object"""
    element = self.head
    self.head = self.head._next
    self._len -= 1
    
    return element


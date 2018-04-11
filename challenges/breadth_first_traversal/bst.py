class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, iter=[]):
        self.root = None
        if isinstance(iter, list):
            for i in iter:
                self.insert(i)

    def insert(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            return
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = node
                    return
                cur = cur.left
            if val >= cur.val:
                if cur.right is None:
                     cur.right = node
                     return
                cur = cur.right

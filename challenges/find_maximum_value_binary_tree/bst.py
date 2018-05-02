class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        pass

    def post_order(self, visitor):
        if self.left:
            self.left.post_order(visitor)
        if self.right:
            self.right.post_order(visitor)
        visitor(self.val)

    def pre_order(self, visitor):
        visitor(self.val)
        if self.left:
            self.left.pre_order(visitor)
        if self.right:
            self.right.pre_order(visitor)


class BST:
    def __init__(self, iter=()):
        self.root = None
        self._len = 0

        for value in iter:
            if isinstance(value, int):
                self.insert(value)

    def __len__(self):
        return self._len

    def insert(self, value):
        if self.root:
            current = self.root
            while True:
                if current.val == value:
                    return
                if current.val > value:
                    if not current.left:
                        current.left = Node(value)
                        self._len += 1
                        return
                    current = current.left
                else:
                    if not current.right:
                        current.right = Node(value)
                        self._len += 1
                        return
                    current = current.right
        else:
            self.root = Node(value)
            self._len += 1

    def post_order(self, visitor):
        if self.root:
            self.root.post_order(visitor)

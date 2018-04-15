class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BST:
    """
    Binart Search Tree has 3 methods to sort nodes byself.
    .inorder(), .preorder(), and .postorder()
    """
    def __init__(self, arr=()):
        self.root = None
        if len(arr):
            for element in arr:
                self.insert(element)

    def in_order(self, operation):
        """
        In order traversal. Traverses nodes starting from head down to the left
        node until val is None than continues to move down right and repeats.
        """
        def _walk(node=None):
            """walk finction jump from node to node"""
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)
            operation(node.val)

            if node.right is not None:
                _walk(node.right)

        if self.root is None:
            return False
        else:
            _walk(self.root)

    def pre_order(self, operation):
        """
        Preorder traversal. Traverses nodes from top to left then right.
        Value of nodes is not considered.
        """
        def _walk(node=None):
            if node is None:
                return
            operation(node.val)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

        if self.root is None:
            return False
        else:
            _walk(self.root)

    def post_order(self, operation):
        """
        Postorder traversal. Traverses nodes from bottom left to the right side
        of the tree in order to collect all nodes in order then collects roots.
        """
        def _walk(node=None):
            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)
            operation(node.val)

            if node is None:
                return

        if self.root is None:
            return False
        else:
            _walk(self.root)

    def insert(self, value):
        """
        Insert node into binary Tree
        input <---- value for new node.
        output <--- newly created node with value
        """
        node = Node(value)

        if self.root is None:
            self.root = node
            return node

        current = self.root
        while current is not None:
            if value >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break
            elif value < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break
        return node

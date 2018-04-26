class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = []
        for node in children:
            self.children.append(Node(node))

    def __repr__(self):
        """Node representation"""
        return 'Instance of Node with value of {}.'.format(self.val)

    def __str__(self):
        """User Node representation"""
        return str(self.val)


class KTree:
    """
    INPUT    <---- VALUE (HEAD NODE)
    OUTPUT   <---- SORTED TREE (BFT, PRE-ORDER, or POST-ORDER method)
    """
    def __init__(self, value):
        """Initializer for K-ary Tree."""
        self.root = Node(value)

    def __repr__(self):
        """K-ary tree representation"""
        return 'Instance of K-ary Tree. Root: {}.'.format(self.root.val)

    def __str__(self):
        """User friendly K-ary tree representation"""
        compressed_tree = []
        self.pre_order(lambda node: compressed_tree.append(str(node.val)))
        return ", ".join(compressed_tree)

    def insert(self, val, parent):
        """
        1st parameter takes any value that gets assigned to parent node.
        2nd parameter takes in an existing node(Parent) that will extend its
        children.
        """
        self.breadth_first_traversal(
            lambda node: node.children.append(Node(val)) if node.val == parent else False)

    def breadth_first_traversal(self, operation):
        """
        BreadthFirst traversal. Appends every node starting from the parent and
        traverses tree by level of 1 to end(preforms operation on each node).
        """
        def recurse(nodelist):
            new_list = []
            for node in nodelist:
                operation(node)
                [new_list.append(child) for child in node.children]
            if len(new_list):
                recurse(new_list)
        if self.root:
            recurse([self.root])

    def _walk(self, node, operation, order):
        """operation is picked depending on the sort method used on tree"""
        if node is None:
            return
        if order == 'pre_order':
            operation(node)
        if len(node.children):
            for child in node.children:
                self._walk(child, operation, order)
        if order == 'post_order':
            operation(node)

    def pre_order(self, operation):
        """Pre-Order traversal on k-ary tree"""
        self._walk(self.root, operation, 'pre_order')

    def post_order(self, operation):
        """Post-Order traversal on k-ary tree"""
        self._walk(self.root, operation, 'post_order')

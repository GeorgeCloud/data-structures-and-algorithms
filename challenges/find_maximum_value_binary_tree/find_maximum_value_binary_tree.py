from bst import BST as tree


def findMaxValue(tree):
    """Return node with highest value in Binary Tree."""
    maximum = None

    def op(val):
        nonlocal maximum
        if maximum is None or val > maximum:
            maximum = val
        else:
            pass

    tree.post_order(op)

    return maximum

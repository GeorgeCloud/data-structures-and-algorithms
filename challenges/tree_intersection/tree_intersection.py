def tree_intersection(tree1, tree2):
    """
    INPUT  <--- (Binary Tree Object, Binary Tree Object)
    OUTPUT <--- [ARRAY WITH NON-UNIQUE VALUES]
    Joins only non-unique nodes from two binary trees.
    """
    setA, setB = set(), []
    tree1.in_order(setA.add)
    tree2.in_order(setB.append)
    return [el for el in setB if el in setA]

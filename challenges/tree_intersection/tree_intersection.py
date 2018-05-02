def tree_intersection(tree1, tree2):
    setA, setB = set(), []

    tree1.in_order(setA.add)
    tree2.in_order(setB.append)
    return [el for el in setB if el in setA]

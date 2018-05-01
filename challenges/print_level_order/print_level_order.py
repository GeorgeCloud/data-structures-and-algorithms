from k_tree import KTree


def print_level_order(tree):
    """
    input  <--- Tree
    output <--- Prints nodes level by level
    """
    if not isinstance(tree, KTree):
        raise TypeError('argument must be of type <KTree>')

    all_strings = []  # For testing output

    def recurse(nodelist):
        nonlocal all_strings
        new_list = []
        printlist = []
        for node in nodelist:
            printlist.append(str(node.val))
            for child in node.children:
                new_list.append(child)

        string = ' '.join(printlist)
        all_strings.append(string)

        if len(new_list):
            recurse(new_list)

    if tree.root:
        recurse([tree.root])

    return '\n'.join(all_strings)

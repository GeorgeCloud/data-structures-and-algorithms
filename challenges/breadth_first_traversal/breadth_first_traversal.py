from bst import BST

def breadthFirstTraversal(bst):
    '''
    Traverses Tree and preforms operation
    for each node in from left to write.

    input <------ bst
    out <--------- print(node.val)
    '''
    cont = []
    if not isinstance(bst, BST):
        raise TypeError('Type Error occurred only accepts BINARY TREE')

    def _walk(nodelist):
        new_list = []
        for node in nodelist:
            bfl.append(node)
            if node.left:
                new_list.append(node.left)
            if node.right:
                new_list.append(node.right)

        if len(new_list):
            _walk(new_list)
    if bst.root:
        _walk([bst.root])
    for node in cont:
        print(node.val)
    return cont

from .queue import Queue


def print_level_order(tree):
    """
    input  <--- Tree
    output <--- Prints nodes level by level
    """
    if not tree.root:
        return ''
    first_queue = Queue([tree.root])
    second_queue = Queue()

    while first_queue or second_queue:
        if not first_queue:
            temp = first_queue
            first_queue = second_queue
            second_queue = temp
        node = queue.dequeue()

        second_queue.enqueue(child)

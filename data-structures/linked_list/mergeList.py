# from linked_list import LinkedList


def ll_merge(arg2, arg1):
    if arg2._len <= 0 and arg1._len <= 0:
        return False

    if arg2.head is None:
        return arg1
    if arg1.head is None:
        return arg2

    if True:
        ptr_left, ptr_right = arg1.head, arg2.head
        while ptr_right is not None:
            # if ptr_left._next:
            arg1.insert_before(ptr_left.val, ptr_right)
            ptr_left, ptr_right = ptr_left._next, ptr_right._next
        return arg1
    else:
        ptr_left, ptr_right = arg1.head, arg2.head
        while ptr_left is not None:
            arg2.insert_before(ptr_right.val, ptr_left)
            ptr_left, ptr_right = ptr_left._next, ptr_right._next
        return arg2


# arr1 = LinkedList([2, 3, 4, 5])
# arr2 = LinkedList([5, 6, 7, 8])
#
# b = ll_merge(arr1, arr2)
#
# print(b)

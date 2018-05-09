def quickSort(arr):
    left, right, piv = None, None, arr[-1]
    # piv = sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]
    for element in arr:
        if element > piv:
            left = arr.index(element)
    for element in arr[::-1][1:]:
        if element < piv:
            # Swaps leftGreatest & RightLowest
            right = arr.index(element)

    arr[left], arr[right] = arr[right], arr[left]
    return arr

print (quickSort([34, 19, 42, 9, 2099, 2018, 0, 2005, 77, 66]))

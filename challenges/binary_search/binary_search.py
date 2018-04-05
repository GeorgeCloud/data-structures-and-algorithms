def binary_search(arr, val):
    """
    Returns val's index in arrayself.
    arr is your array.
    val is the index you want to find in your array.
    """
    first, last = 0, len(arr)-1
    while first <= last and first != last:
        if (first + last) % 2:
            middle = (first + last + 1) // 2
        else:
            middle = (first + last) // 2
        if arr[middle] == val:
            return middle
        if arr[middle] > val:
            last = middle - 1
        else:
            first = middle
    return -1


# print(binary_search([1, 2, 3, 4, 5, 6], 6))

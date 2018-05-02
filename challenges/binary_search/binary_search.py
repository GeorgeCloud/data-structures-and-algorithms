def binarySearch(arr, val):
    """
    Searches through an array for search value and returns index
    Input <--- array & search value
    Output <--- index of search value if found. If not returns -1
    """
    if len(arr) < 1:
        return -1
    first, last = 0, len(arr) - 1
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

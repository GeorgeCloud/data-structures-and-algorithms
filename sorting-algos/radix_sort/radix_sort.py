def radixSort(arr):
    """Sorts an unordered array using the radix sort method."""
    n = len(str(max(arr)))
    queue = [[] for i in range(10)]
    for loop in range(0, n):
        for curr in arr:
            queue[int(curr/10**loop % 10)].append(curr)
        del arr[:]
        for bucket in queue:
            arr.extend(bucket)
            del bucket[:]
    return arr

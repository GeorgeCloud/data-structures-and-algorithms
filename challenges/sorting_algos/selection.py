def selectionSort(arr):
    for ele in range(len(arr)-1, 0, -1):
        curr = 0
        for location in range(1, ele + 1):
            if arr[location] > arr[curr]:
                curr = location

        temp = arr[ele]
        arr[ele] = arr[curr]
        arr[curr] = temp
    return arr

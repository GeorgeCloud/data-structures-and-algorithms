def largest_product(arr):
    """
    Accepts matrix array and return the largest product of
    2 adjacent values within the 2D array.
    """
    max = arr[0][0] * arr[1][0]
    row = 0
    for i in range(len(arr) - 1):
        col = 0
        arr = arr[row][0] * arr[row + 1][0]
        if arr > max:
            max = arr
        for _ in range(len(arr[0]) - 1):
            arr1 = arr[row][col] * arr[row][col + 1]
            arr2 = arr[row + 1][col] * arr[row + 1][col + 1]
            arr3 = arr[row][col + 1] * arr[row + 1][col + 1]
            arr4 = arr[row][col] * arr[row + 1][col + 1]
            arr5 = arr[row][col + 1] * arr[row + 1][col]
            if arr1 > max:
                max = arr1
            if arr2 > max:
                max = arr2
            if arr3 > max:
                max = arr3
            if arr4 > max:
                max = arr4
            if arr5 > max:
                max = arr5
            col += 1
        row += 1
    return max

print(largest_product([[1,2],[3,4],[5,6],[7,8]]))

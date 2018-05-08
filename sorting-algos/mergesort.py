def mergesort(arr):
    """Sorts a unsorted array"""
    def move(left, right, arr):
        """Recursive call."""
        arr = [0]*(len(left)+len(right))
        i = j = 0
        while i+j < len(arr):
            if j == len(right) or i < len(left) and left[i] < right[j]:
                arr[i+j] = left[i]
                i += 1
            else:
                arr[i+j] = right[j]
                j += 1
        return arr
    if len(arr) < 2:
        return arr
    temp = []
    midle = len(arr)//2
    left, right = arr[:midle], arr[midle:]
    a, b = mergesort(left), mergesort(right)
    curr = move(a, b, temp)
    return curr

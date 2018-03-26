testArray = ['phone', 'pop', 'tree', 'item']



def insertShiftArray(arr, value):
    """
    Adding the users input value if current element in iteration
    is the element in given arrays length - 1
    """
    newArray = []
    for i in arr:
        if i == arr[len(arr)/2-1]:
            print i, 'is equal to (middle-1) element: ', arr[len(arr)/2-1]
            newArray += i; newArray += value
        else:
            print 'inserting items from testArray'
            newArray += i
    return newArray


# print insertShiftArray(testArray, 'e')

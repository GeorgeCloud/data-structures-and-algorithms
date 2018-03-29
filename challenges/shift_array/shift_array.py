def insertShiftArray(arr, val):
    """Inserts value in the middle of an array"""
    try:
        if type(arr) != list:
            raise TypeError('First variable is suppose to be an array type')
    except TypeError as err:
        print(err.args[0])
        return False

    if len(arr) == 0:
        return [val]

    new_array = []
    for i in range(len(arr)):
        if i >= len(arr)/2 and i < len(arr)/2+1:
            new_array.append(val)
        new_array.append(arr[i])
    return new_array

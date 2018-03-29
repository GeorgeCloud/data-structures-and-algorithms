import shift_array

# Array of size 4
testArray = ['phone', 'pop', 'tree', 'item']


def test_insertShiftArray_type():
    """Checks if input is only array"""
    arr = shift_array.insertShiftArray(2, 4)
    assert arr is False


def test_insertShiftArray_length():
    """Checks for length aftering inserting value into array"""
    arr = shift_array.insertShiftArray(testArray, 100)
    assert len(arr) == 5


def test_insertShiftArray_value_inserted():
    """Checks if input is the valid value being compared to"""
    arr = shift_array.insertShiftArray(testArray, 'movie')
    assert arr[int(len(arr)/2)] == 'movie'

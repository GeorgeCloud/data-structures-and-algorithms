from shift_array import *

def test_insertShiftArray_length(testArray, 'e'):
    assert insertShiftArray(testArray, 'e') == len(testArray) + 1

def test_insertShiftArray_value_inserted(testArray, 'e'):
    assert insertShiftArray(testArray, 'e') == testArray.insert(len(testArray/2), e)

def test_insertShiftArray_length_type(testArray, 'e'):
    assert isinstance(insertShiftArray(testArray, 'e'), list)
    

import pytest
from hash_table import HashTable
from left_join import left_join


@pytest.fixture
def empty_tables():
    return HashTable(), HashTable()


@pytest.fixture
def empty_left_table():
    rightTable = HashTable()
    rightTable.set('a', 5)
    return HashTable(), rightTable


@pytest.fixture
def empty_right_table():
    leftTable = HashTable()
    leftTable.set('a', 5)
    return leftTable, HashTable()


# SET UP FOR FIRST HASHTABLE
hashtable1 = HashTable()
hashtable1.set('a', 5)
hashtable1.set('8', 523)

# SET UP FOR SECOND HASHTABLE
# SHARES ONE ELEMENT WITH HASHTABLE ONE
hashtable2 = HashTable()
hashtable2.set('z', 77)
hashtable2.set('a', 63)


def test_invalid_size_ht():
    with pytest.raises(ValueError):
        table = HashTable(-1)
        # Does not reach here
        return table


def test_empty_left(empty_left_table):
    """Validates None is returned if left table has no elements"""
    assert left_join(empty_left_table[0], empty_left_table[1]) is None


def test_empty_right(empty_right_table):
    """Validates that the left is the only value present"""
    assert left_join(empty_right_table[0], empty_right_table[1]).get('a') == [5, None]


def test_left_simple_join():
    """Validaes that two tables return the common key/values"""
    assert left_join(hashtable1, hashtable2).get('a') == [5, 63]

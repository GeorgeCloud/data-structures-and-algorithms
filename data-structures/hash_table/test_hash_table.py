from hash_table import HashTable
import pytest


@pytest.fixture
def empty_table():
    """Empty hash table."""
    return HashTable()


@pytest.fixture
def single_element_table():
    """One LinkedList element."""
    return HashTable(1)


def test_hash_table_max_size():
    """Validates if the number given can make a valid amount of elements inside
    the hash table."""
    with pytest.raises(ValueError):
        HashTable(0)


def test_hash_key_invalid_arg(empty_table):
    """Test non-string passed to _hash_key raises."""
    with pytest.raises(TypeError):
        empty_table.hash_key(4)


def test_hash_table_max_size_type():
    """Test invalid max_size arg raises."""
    with pytest.raises(TypeError):
        HashTable('type')


def test_hash_key_valid(empty_table):
    """Test string hash's index."""
    assert empty_table.hash_key('abc') == 294
    assert empty_table.hash_key('abcdefghijklmnopqrstuvwxyz') == 799


def test_hash_key_single_valid(single_element_table):
    """Test strings are equal to index in hash."""
    assert single_element_table.hash_key('abc') == 0
    # assert single_element_table.hash_key('abcdefghijklmnopqustuvwxyz') == 0


def test_set_invalid_arg(empty_table):
    """Test raises."""
    with pytest.raises(TypeError):
        empty_table.set(1)


def test_set_key_invalid_none_types(empty_table):
    """Testing is invalids ouput none values."""
    empty_table.set('new', 'e')
    empty_table.set('outside', 'u')
    assert empty_table.buckets[294].head is None
    assert empty_table.buckets[799].head is None


def test_set_key_valid_single(single_element_table):
    """Test simple element table by asserting values."""
    single_element_table.set('new', 'n')
    single_element_table.set('newa', 'e')
    assert single_element_table.buckets[0].head.val['newa'] == 'e'
    assert single_element_table.buckets[0].head._next.val['new'] == 'n'


def test_get_invalid_keys(empty_table):
    """Test getting with non-string raises."""
    with pytest.raises(TypeError):
        empty_table.set(1)


def test_get_key_valid_keys(empty_table):
    """Test empty buckets."""
    empty_table.set('new', 1)
    empty_table.set('newa', 2)
    assert empty_table.get('new') == 1
    assert empty_table.get('newa') == 2


def test_get_key_valid_single(single_element_table):
    """Test retrieval for single buckets."""
    single_element_table.set('new', 1)
    single_element_table.set('newa', 2)
    assert single_element_table.get('new') == 1
    assert single_element_table.get('newa') == 2


def test_remove_invalid_max(empty_table):
    """Test removing option for buckets."""
    with pytest.raises(TypeError):
        empty_table.set(1)


def test_remove_all(single_element_table):
    """Test emptying bucket."""
    single_element_table.set('new', 1)
    single_element_table.set('newa', 2)
    single_element_table.remove('newa', True)
    assert single_element_table.get('new') is None

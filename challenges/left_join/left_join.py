from hash_table import HashTable


def left_join(table_1, table_2):
    """
    No additional __iter__ for LinkedList or hash_table.
    Joins elements from table2 if their key is identical.
    """
    new_hash = HashTable()
    table1_keys = [list(keys1.head.val)[0] for keys1 in table_1.buckets if keys1.head is not None]
    table2_keys = [list(keys2.head.val)[0] for keys2 in table_2.buckets if keys2.head is not None]
    if not table1_keys:
        return None
    for x in table1_keys:
        if x in table2_keys:
            new_hash.set(x, [table_1.get(x), table_2.get(x)])
        else:
            new_hash.set(x, [table_1.get(x), None])
    return new_hash

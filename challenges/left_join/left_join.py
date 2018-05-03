from hash_table import HashTable


def left_join(table_1, table_2):
    """Joins elements from table2 if their key is identical."""
    left_joined = {}
    for key in table_1:
        left_joined[key] = [table_1.get(key), 'NULL']
    for key in table_2:
        if key in left_joined:
            left_joined[key][1] = table_2.get(key)

    return left_joined


table1 = HashTable()
table1.set('a', 5)
tableFin = set()
for i in table1.buckets:
    if i.head is not None:
        x = i.head.val
        print(x)
        # print(5 in i.head.val.values())

# for k in table1.buckets:
#     if i.head is not None and i.head.keys


table2 = HashTable()
table2.set('b', 6)
# print(table2)

# left_join(table1, table2)

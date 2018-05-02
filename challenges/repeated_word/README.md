# First repeated word
A hash table is a data structure which implements an associative array. It uses
keys to values for look up. The hash table uses buckets(linked_lists) for storage
and lookup.

## Challenge
Having to iterate through a string an add it to the has function and implement
the ability to keep count. And if the occurrence is ever twice for a single word
then return that else return False.

## Solution
Iterate through string and add it to a dictionary inside the hash table. If the
element already exists then return that value automatically without updating the
count. Else return False if you reach the end without reaching a duplicate
element.

from linked_list import LinkedList


class HashTable:
    """Hash table template."""
    def __init__(self, max_size=1024):
        if max_size < 1:
            raise ValueError('Invalid HashTable size.')
        self.max_size = max_size
        self.buckets = [LinkedList() for _ in range(max_size)]

    def hash_key(self, val):
        """Converts value given into unicode repr."""
        if type(val) is not str:
            raise TypeError('Invalid type. Must be string type.')
        return sum(map(lambda x: ord(x), val)) % self.max_size

    def set(self, key, val):
        """Insert value into hash table."""
        if type(key) is not str:
            raise TypeError('Not a string can\'t convert into unicode.')
        return self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key):
        """Return value by index inside hastable."""
        if type(key) is not str:
            raise TypeError('Invalid input type.')

        curr = self.buckets[self.hash_key(key)].head
        while curr:
            if key in curr.val.keys():
                return curr.val[key]
            curr = curr._next

    def remove(self, key, flag=False):
        """Removes bucket by searching for index in table."""
        ll = self.buckets[self.hash_key(key)]
        runner = ll.head
        prev = runner
        while runner:
            if key in runner.val.keys():
                if flag:
                    ll.head = None
                else:
                    if prev is not runner:
                        prev._next = runner._next
                    else:
                        ll.head = runner._next
                return runner.val[key]
            prev = runner
            runner = runner._next

#!python

from linked_list import LinkedList


class HashTable(object):

    def __init__(self, num_buckets=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(num_buckets):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0

        for bucket in self.buckets:
            for item in bucket.items():
                count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket_id =hash(key) % len(self.buckets)
        bucket_ll = self.buckets[bucket_id]

        node = bucket_ll.head

        while node is not None:
            if key == node.data[0]:
                return True
            node = node.next
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_id =hash(key) % len(self.buckets)
        bucket_ll = self.buckets[bucket_id]

        node = bucket_ll.head

        while node is not None:
            if key == node.data[0]:
                return node.data[1]
            node = node.next
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket_id = hash(key) % len(self.buckets)
        bucket_ll = self.buckets[bucket_id]

        # check if key is in the ll, find method()
        current = bucket_ll.head
        while current is not None:
            # (key,value)
            if key == current.data[0]:
            # update hash table value
                current.data = (key, value)
                return
            current = current.next
        # if no key, insert new (key,value) tuple

        bucket_ll.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        value = self.get(key)
        if value is not None:
            bucket_id = hash(key) % len(self.buckets)
            bucket_ll = self.buckets[bucket_id]
            bucket_ll.delete((key,value))


if __name__ == '__main__':
    ht = HashTable(5)
    print('hash table: {}'.format(ht))
    #testing insert new
    ht.set("unicorn", 10)
    ht.set("tiger", 11)
    print(ht) #should see unicorn,10 and tiger 11
    #test insert update
    ht.set("unicorn", 99)
    print(ht) # should see unicorn 99 and tiger 11


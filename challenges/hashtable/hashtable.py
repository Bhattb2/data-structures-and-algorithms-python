from linkedlist import LinkedList


class HashTable:

    def __init__(self, size=1024):
        self.size = size
        self.bucket = [None] * size


    def hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)

        sum = sum * 199 # using prime number but could be anything you want, such as ascii of first char

        return sum % self.size


    def add(self, key, value):
    
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
           self._buckets[hashed_key] = LinkedList()
        
        self._buckets[hashed_key].append([key, value])


    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self._bucket[hashed_key]

        if bucket:
            current = bucket.head

            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next


    def contains(self, key):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            return False
        else:
            bucket = self._buckets[hashed_key]
            current = bucket.head

            while current:
                if current.data[0] == key:
                    return True
                current = current.next


hashtable = HashTable()
hashtable.add('Bhag', 10)
hashtable.add('Mina', 11)
hashtable.add('ujaR', 14)
hashtable.add('anyaN', 15)
hashtable.add('Dhar', 18)
hashtable.add('Dipti', 19)
hashtable.add('Malti', 20)

for item in hashtable._buckets:

    if item:
        item.display()

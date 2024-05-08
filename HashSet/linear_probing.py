class MyHashSet:

    def __init__(self):
        self.size = 10000 # defines the size of the hashset
        self.slot = [None] * self.size
        self.n = 0 # Will maintain the number of elements in the hashset

    def add(self, key: int) -> None:

        if not self.find(key):
            if self.n == self.size:
                self.resize()
                
            self.__add_item(key)

            # self.n += 1

            # print(self.slot)

    def __add_item(self, key):

        hash_value = self.hash_function(key)

        while self.slot[hash_value] not in [None, 'Deleted']:
            hash_value = self.rehash_function(hash_value)
            
        self.slot[hash_value] = key
        self.n += 1


    def resize(self):
        self.size = self.size*2
        old_list = self.slot
        self.n = 0

        self.slot = [None] * self.size

        for i in old_list:
            if i not in [None, 'Deleted']:
                self.__add_item(i)

    def remove(self, key: int) -> None:
        hash_value = self.find(key)
        if hash_value is not None:
            self.slot[hash_value] = 'Deleted'
            self.n -= 1
        
        # print(self.slot)
        
    def contains(self, key: int) -> bool:
        return self.find(key) is not None

    def find(self, key):
        hash_value = self.hash_function(key)
        original_hash_value = hash_value

        while self.slot[hash_value] != key:
            if self.slot[hash_value] is None: # In linear probing elements move ahead one by one
                return None
            hash_value = self.rehash_function(hash_value)
            if hash_value == original_hash_value:
                    return None

        # print(self.slot)
        
        return hash_value

    def hash_function(self, key):
        return hash(key) % self.size

    def rehash_function(self, old_hash_value):
        return (old_hash_value + 1) % self.size

class MyHashSet:

    def __init__(self):
        self.size = 100000 # defines the size of the hashset
        self.slot = [None] * self.size
        self.n = 0 # Will maintain the number of elements in the hashset

    def add(self, key: int) -> None:

        if not self.find(key):
            if self.n == self.size:
                self.resize()
                
            self.__add_item(key)

    def __add_item(self, key):

        original_hash_value = self.hash_function(key)
        current_hash_value = original_hash_value
        counter = 0

        while self.slot[current_hash_value] not in [None, 'Deleted']:
            counter += 1
            current_hash_value = self.quadratic_hash_function(original_hash_value, counter)
            
        self.slot[current_hash_value] = key
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
        
    def contains(self, key: int) -> bool:
        return self.find(key) is not None

    def find(self, key):
        original_hash_value = self.hash_function(key)
        current_hash_value = original_hash_value
        counter = 0

        while self.slot[current_hash_value] != key:
            counter += 1
            if self.slot[current_hash_value] is None: # this can be problematic if using quadratic probing
                return None
            current_hash_value = self.quadratic_hash_function(original_hash_value, counter)
            if current_hash_value == original_hash_value:
                    return None
        
        return current_hash_value

    def hash_function(self, key):
        return hash(key) % self.size

    def rehash_function(self, old_hash_value):
        return (old_hash_value + 1) % self.size

    def quadratic_hash_function(self, base_hash, counter):
        return (base_hash + counter**2) % self.size

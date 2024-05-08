from typing import Union

class MyHashMap:

    def __init__(self):
        self.size = 10000 # Refers to the size of the Dictionary
        self.n = 0 # Refers to the number of nodes in the Dictionary
        self.keys = [None for i in range(self.size)]
        self.values = [None for i in range(self.size)]


    def put(self, key: int, value: int) -> None:
        """
            This method will add a key-value pair to the HashMap. If the key already exists then it will just replace the value
        """

        if self.n == self.size:
            self.resize()

        self.__put(key, value, 0)

    
    def __put(self, key: int, value: int, resize: bool) -> None:

        # this is an optimisation to ensure that we don't check for the key when resizing
        if not resize:
            # check if key exists - if key exists then change value
            index = self.key_exists(key)

            if index is not None:
                self.values[index] = value
                return

        # if key does not exist then add key-value pair to the dictionary
        original_hash_value = self.hash_function(key)
        current_hash_value = original_hash_value
        counter = 1

        while self.keys[current_hash_value] not in [None, 'Deleted']:
            current_hash_value = self.quadratic_rehash_function(original_hash_value, counter)
            counter += 1
            
        self.keys[current_hash_value] = key
        self.values[current_hash_value] = value

        self.n += 1
        
    def resize(self) -> None:

        self.size = self.size * 2
        self.n = 0
        old_keys = self.keys
        old_values = self.values

        self.keys = [None for i in range(self.size)]
        self.values = [None for i in range(self.size)]

        for key, value in zip(old_keys, old_values):
            self.__put(key, value, resize=1)

    def get(self, key: int) -> int:
        """
            Given a key, this method will return the value. If the key does not exist it will return -1
        """

        index = self.key_exists(key) # If key does not exist then output will be None else the index where it is located

        if index is not None:
            return self.values[index]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
            Given a key, this method will remove the key-value pair from the Hash Map. It will not return anything (even if key is not present)

            Note: We are deliberately provide a separate tag when deleting a key-value pair instead of None. Imagine if another element with the same initial hash value has to be searched in the dictionary. Because the current index is occupied (by the key-value pair we deleted) we will end up putting it in another slot. But currently to optimize our Search logic we have written then when you find a 'None' stop searching. Therefore you can end up in a situation where you retrieve key-value not found despite it being there
        """

        index = self.key_exists(key)

        if index is not None:
            self.keys[index] = 'Deleted'
            self.values[index] = 'Deleted'
        

    def key_exists(self, key: int) -> Union[int, None]:

        original_hash_value = self.hash_function(key)
        current_hash_value = original_hash_value
        counter = 1

        while self.keys[current_hash_value] is not None:
            if self.keys[current_hash_value] == key: # This means that key was found
                return current_hash_value

            current_hash_value = self.quadratic_rehash_function(original_hash_value, counter) # Computing the new hash value

            if current_hash_value == original_hash_value: # This means that you've travelled the entire list and come back to the original hash value which means key does not exist
                return None

            counter += 1

    def hash_function(self, key: int) -> int:
        return hash(key) % self.size

    def quadratic_rehash_function(self, original_hash_value: int, counter: int) -> int:
        return (original_hash_value + (counter**2)) % self.size
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class Node:

    def __init__(self, key:int, value: int) -> None:
        self.key = key
        self.value = value
        self.next = None # How to add data type here

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def insert_from_tail(self, key: int, value: int) -> None:
        """
            This method will insert a key-value pair into a LinkedList from the tail. Edge cases to take care of:
                - When size of LL = 0 => head and tail will point to same node
        """
        
        # Create a new node
        new_node = Node(key, value)
        
        # Check if size of LL is 0
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        # Increase the node count by 1
        self.n += 1

    def add_or_replace(self, key: int, value: int) -> None:
        """
            This method will traverse the LL and see if the "key" exists. If it does, then it will change its value. If it does not exist then it will insert the key-value pair from the tail

            Note: For optimization sake, we aren't using a separate "key_exists" or "get" method because even if we knew that a key existed, we'd still have to traverse it to replace it => the optimization is miniscule i.e. O(2n) -> O(n)
        """

        if self.tail.key == key: # Optimisation: Ensuring that we don't traverse the entire LL if the key is the tail node (no such optimsation needed if key is in head node because the loop will only run once)
            self.tail.value = value
            return

        current_node = self.head

        while current_node is not None: # This logic takes of the situation when self.n = 0 (because this loop won't run)
            if current_node.key == key:
                current_node.value = value
                return
            current_node = current_node.next
        
        self.insert_from_tail(key, value)

    def get(self, key: int) -> int:
        """
            Given a key, this method will return the value associated with that key. If the key does not exist then it will return -1
        """

        if self.tail.key == key: # Optimisation: Ensuring that we don't traverse the entire LL if the key is the tail node (no such optimsation needed if key is in head node because the loop will only run once)
            return self.tail.value

        current_node = self.head

        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next

        return -1

    def remove(self, key:int) -> None:
        """
            Given a key, this method will remove the key-value pair from the LL. If no such key exists then it will return nothing

            Note: In this method the tail optimization will not work because you cannot move in the reverse direction in a single LL. Even if you knew that the 'key' is present in the tail, you can only go in the forward direction (becuase when deleting from tail node, you'll have to move the tail node in the reverse direction which is not possible)

            This method does not have different messages for different exit conditions i.e. this method provides null as the return value even if the key is not present, the LL is empty or even if you deleted the key-value. If you want separate messages then you'll have to make changes in the code
        """

        previous_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.key == key:
                if previous_node is None: # This means that matching node is a head node
                    if self.head == self.tail: # This means that there is only one element in the node (matching node = head)
                        self.head = None
                        self.tail = None
                        self.n = 0
                        return
                    else:                       # This means that there are multiple nodes (matching node = head)
                        self.head = current_node.next
                        current_node = None
                        self.n -= 1
                        return
                
                elif current_node.next is None: # This means that the matching node is a tail node
                    self.tail = previous_node
                    previous_node.next = None
                    self.n -= 1
                    return
                
                else:                        # This means that matching node is in between
                    previous_node.next = current_node.next
                    current_node.next = None
                    self.n -= 1
                    return
            
            previous_node = current_node
            current_node = current_node.next
        
        # If no node was found
        return
     

class MyHashMap:

    def __init__(self):
        self.buckets = 1000 # Refers to the size of the Dictionary
        self.n = 0 # Refers to the number of nodes in the Dictionary
        self.slot = [LinkedList() for i in range(self.buckets)]

    def put(self, key: int, value: int) -> None:
        """
            This method will add a key-value pair to the HashMap. If the key already exists then it will just replace the value
        """

        # Check the load factor. Resize if load factor > 2
        if self.n / self.buckets > 2:
            self.resize()
        
        # Call the __put method to add key-value to the HashMap
        self.__put(key, value)
        
    
    def __put(self, key: int, value: int) -> None:

        # Compute hash value of key
        hash_value = self.hash_function(key)

        # If the LinkedList in the hash value position of self.slot is empty -> insert node from tail (Ex: if hash value = 2, check if LL in self.slot[2] is empty)
        if self.slot[hash_value].head is None:
            self.slot[hash_value].insert_from_tail(key, value)

        # If the LinkedList has other nodes present in it -> check if key is already present. If present, then change value else insert key-value pair from tail
        else:
            self.slot[hash_value].add_or_replace(key, value)
        
        # Increment node count by 1
        self.n += 1

    def resize(self) -> None:
        self.buckets = self.buckets * 2
        self.n = 0
        old_slot = self.slot

        self.slot = [LinkedList() for i in range(self.buckets)]

        for LL in old_slot:
            if LL.head is not None:

                current_node = LL.head

                while current_node is not None:
                    self.__put(current_node.key, current_node.value)
                    current_node = current_node.next


    def get(self, key: int) -> int:

        # Compute the hash value of the key
        hash_value = self.hash_function(key)

        # If hash value index has empty LL then return -1 (because key does not exist - if it did LL wouldn't be empty)
        if self.slot[hash_value].head is None:
            return -1
        # If LL is not empty then call the LL's .get() method
        else:
            value = self.slot[hash_value].get(key)
            return value
        

    def remove(self, key: int) -> None:

        # Compute the hash value of the key
        hash_value = self.hash_function(key)

        # If hash value index has empty LL then return nothin (because key does not exist - if it did LL wouldn't be empty)
        if self.slot[hash_value].head is None:
            return

        # If LL is not empty then call the LL's .remove() method
        else:
            self.slot[hash_value].remove(key)
            return


    def hash_function(self, key: int) -> int:
        return hash(key) % self.buckets
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

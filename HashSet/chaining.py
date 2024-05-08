class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def add_from_tail(self, value):
        # Create new node
        new_node = Node(value)

        # If LinkedList is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If LinkedList is not empty
        else:
            self.tail.next = new_node
            self.tail = new_node

        # Increase node count by 1
        self.n += 1

    def node_exists(self, value):
        
        # Check if node is present in tail. This can make search O(1)
        if self.tail.value == value:
            return True

        # If node is not present in tail then iterate through list
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        
        return False

    def delete_node(self, value):

        previous_node = None
        current_node = self.head

        while current_node is not None:
            # Check if any node value matches with the provided value
            if current_node.value == value:

                # Check if the node is a head node
                if previous_node is None:
                    self.head = current_node.next

                    # This will take care of the scenario where LL was originally of size 1 (after deletion = 0)
                    if self.head is None:
                        self.tail = None
                
                # Check if node is tail node
                elif current_node.next is None:
                    self.tail = previous_node
                    previous_node.next = None
                
                # If node is in the middle
                else:
                    previous_node.next = current_node.next
                    current_node.next = None
                
                self.n -= 1
                return
            
            previous_node = current_node
            current_node = current_node.next
    
        return 

    def __str__(self):
        current_node = self.head
        output = ""

        while current_node != None:
            output += str(current_node.value) + " -> "
            current_node = current_node.next

        return output[: -4]     

class MyHashSet:

    def __init__(self):
        self.size = 4999 # defines the size of the hashset
        self.slot = [LinkedList() for i in range(self.size)]
        self.n = 0 # Will maintain the number of elements in the hashset

    def add(self, key: int) -> None:

        # If key is already present in hash set then don't add it
        if self.contains(key):
            return

        # If load factor is crossed then resize the hash set
        if self.n / self.size > 2:
            self.resize()

        self.__add_item(key)

        self.n += 1

    def __add_item(self, key):
        # Create hash value of the key
        hash_value = self.hash_function(key)

        # Add element from the tail
        self.slot[hash_value].add_from_tail(key)    

    def resize(self):
        self.size = self.size*2
        old_list = self.slot

        self.slot = [LinkedList() for i in range(self.size)]

        for LL in old_list:
            if LL.head is not None:
                current_node = LL.head

                while current_node != None:
                    self.__add_item(current_node.value)
                    current_node = current_node.next

    def remove(self, key: int) -> None:
        
        # find the hash-value
        hash_value = self.hash_function(key)

        # check if linked list is non-empty at the particular index
        if self.slot[hash_value].head == None:
            return
        # delete node - if not found then pass
        else:
            self.slot[hash_value].delete_node(key)

    def contains(self, key: int) -> bool:
        
        hash_value = self.hash_function(key)

        # Check if LinkedList is empty
        if self.slot[hash_value].head is None:
            return False

        # Call the node_exists() method from the LinkedList class to see if key exists
        if self.slot[hash_value].node_exists(key):
            return True
        else:
            return False

    def hash_function(self, key):
        return hash(key) % self.size

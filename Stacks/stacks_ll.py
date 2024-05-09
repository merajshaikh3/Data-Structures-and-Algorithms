class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.n = 0

    def push(self, value):
        # Create a node with provided value
        new_node = Node(value)

        # Add the node from head
        new_node.next = self.head
        self.head = new_node

        # Increase stack count by 1
        self.n += 1

    def pop(self):
        # check if stack if empty
        if self.n == 0:
            return "Empty Stack"
        # If Stack is not empty
        else:
            # .pop will always remove the current head node
            node_to_pop = self.head

            # the second node in the stack will be re-assigned as the new head node
            self.head = node_to_pop.next

            # Decrease stack count by 1
            self.n -= 1

        # we'll return the node value that was popped off
        return node_to_pop.value
    
    def peek(self):
        if self.n == 0:
            return "Empty Stack"
        else:
            return self.head.value
    
    def isempty(self):
        return self.n == 0
    
    def size(self):
        return self.n

    def __str__(self):
        current_node = self.head
        output = ""

        while current_node != None:
            if isinstance(current_node.value, str):
                output += "'" + str(current_node.value) + "'" + "-> "
            else:
                output += str(current_node.value) + "-> "
            
            current_node = current_node.next
        
        return output[:-3]

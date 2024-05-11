class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
Pointer regarding Queues:
- Instead of a head and tail a queue has a front (head) and rear (tail).
- Properties of front and head are the same i.e. front is the first node in the queue. It has address of the next node in the queue
- Properties of rear and tail are the same i.e. rear is the last node in the queue. It 'next' attribute points to 'None'
- In a queue, you can only add elements from the rear (i.e. tail) and only remove items from the front (i.e. head)
- The above technique is know as FIFO (first in first out)
"""


class Queue:
    def __init__(self):
        self.front = None # This is the 'head' of the queue. Exits will happen from here
        self.rear = None # This is the 'tail' of the queue. Entries will happen from here
        self.n = 0

    def enqueue(self, value):
        # Create new node
        new_node = Node(value)

        # Set the new node as rear
        if self.n == 0:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node # new_node.next will point to None since it is added from the tail
            self.rear = new_node

        # Increase size of queue by 1
        self.n += 1

    def dequeue(self):
        # Check if queue is empty
        if self.n == 0:
            return "Queue is empty. Cannot dequeue"
        else:
            # Set the second node as the "front" node
            self.front = self.front.next
            
            # Reduce size of the Queue by 1
            self.n -= 1

    def is_empty(self):
        return self.n == 0
    
    def size(self):
        return self.n
    
    def front_item(self):
        if self.n == 0:
            return "Empty Queue"
        else:
            return self.front.value
    
    def rear_item(self):
        if self.n == 0:
            return "Empty Queue"
        else:
            return self.rear.value

    def __str__(self):
        current_node = self.front
        output = ""

        while current_node != None:
            if isinstance(current_node.value, str):
                output += "'" + str(current_node.value) + "'" + " <- "
            else:
                output += str(current_node.value) + " <- "
            
            current_node = current_node.next
        
        return output[:-4]

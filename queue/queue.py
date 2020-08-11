from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self): # returns the number of elements in the queue
        return self.size

    def enqueue(self, value): # adds an element to the back of the queue
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self): # removes and returns the element at the front of the queue
        if self.size == 0: # if theres no element
            return None # return none
        else: # if there is an element or elements
            element = self.storage.head.get_value() # assign element to the head value of the queue
            self.storage.remove_head() # remove the head value of the queue
            self.size += -1 # minus 1 on the size of the queue
            return element # return the head element we removed

from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self): # returns the number of elements in the stack
        return self.size

    def push(self, value): # adds an item to the top of the stack
        self.storage.add_to_tail(value) # adds the given value to the top of the stack
        self.size += 1 # plus 1 to the size of the stack

    def pop(self): # removes and returns the element at the top of the stack
        if self.size == 0: # if there is no element
            return None # return none
        else: # if there is elements
            element = self.storage.tail.get_value() # gets the value of the tail
            self.storage.remove_tail() # removes tail
            self.size += -1 # lowers the size of the stack
            return element # returns the tail that was removed
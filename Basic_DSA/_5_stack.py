# Stack

# LIFO -> Last in first out

from collections import deque

class stack:

    def __init__(self):
        self.data = deque()

    # adding the element in stack
    def push(self,element):
        self.data.append(element)

    def isEmpty(self):
        pass
    
    # deleting the last element of stack
    def pop(self):
        pass

    # returning the last element of stack
    def peek(self):
        pass

    def deleteAll(self):
        pass

    def view(self):
        return self.data

obj = stack()
obj.push(34)
print(obj.view())
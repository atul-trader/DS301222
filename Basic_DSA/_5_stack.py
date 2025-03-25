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
        if len(self.data)==0:
            return True
        return False

    # def isEmpty(self):
    #      return self.data == None
    
    # def isEmpty(self):
    #     if self.data == deque([]):
    #         return True
    #     else: 
    #         return False

    # deleting the last element of stack
    def pop(self):
        if self.isEmpty():
            print("Error: Stack is empty, hence cannot pop the element")
        else:
            self.data.pop()

    # returning the last element of stack
    def peek(self):
        if self.isEmpty():
            print("Error: Stack is empty, hence cannot return the last element")
        else:
            return self.data[-1]

    def deleteAll(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.data.clear()

    def view(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.data

obj = stack()
obj.push(34)
obj.push(14)
obj.push(40)
print(obj.view())

print(obj.isEmpty())

# obj.pop()
# print(obj.view())

# element = obj.peek()
# print(element)

obj.deleteAll()
print(obj.view())
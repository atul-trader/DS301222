# Queue
# FIFO - First in first out

class queue:
    def __init__(self):
        self.data = []

    def add(self,element):
        self.data.append(element)
    
    def isEmpty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def size(self):
        if self.isEmpty():
            return 0
        else: 
            return len(self.data)
    
    def deleteAll(self):
        if self.isEmpty():
            return "Error: It's already empty."
        else: self.data.clear()
    
    def viewAll(self):
        if self.isEmpty():
            return "Error: No elements in queue."
        else:
            return self.data
    
    def peek(self):
        if self.isEmpty():
            return "Error: No elements in queue"
        else:
            return self.data[0]
        
    def poll(self):
        if self.isEmpty():
            return "Error: No elements in queue"
        else:
            return self.data.pop(0)

obj = queue()
# obj.add(89)
# obj.add(90)
# obj.add(17)

print(obj.viewAll())

print(obj.size())
# print(obj.peek())

# print(obj.poll())
# print(obj.viewAll())

# obj.deleteAll()
# print(obj.viewAll())
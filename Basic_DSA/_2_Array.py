# Array -----> List

# Array
# -> it accepts heterogenous data (only in python and js)
# -> it doesnot have a fix size (only in python and js)
# -> it is use to store collection of same/differet types of data
# -> fetch the data
# -> insert the data at specify position
# -> remove the data

# lst = []
# lst.append(10)
# lst.extend([1,2,3,4,5])
# lst.insert(1,200)
# lst.remove(200)
# print(lst)

class array:
    def __init__(self,fix_size):
        self.fix_size = fix_size
        self.data = []
        self.length = 0

    def add(self,element):
        if self.length < self.fix_size:
            self.data.append(element)
            self.length += 1
        else:
            print("Error : Array is full")

    def display(self):
        return self.data
        
    def removeByIndex(self,index): 
        for i in range(self.length):
            if i == index:
                self.data.pop(i)
                self.length -= 1
                break
        else:
            print("Error : No such index found")

    def removeByElement(self,element):
        if element in self.data:
            self.data.remove(element)
            self.length -= 1
        else:
            print("No such element found.")

obj = array(5)
obj.add(1)
obj.add(11)
obj.add(21)
obj.add(31)
obj.add(41)
print(obj.display())

# obj.removeByIndex(20)
# print(obj.display())

obj.removeByElement(44)
print(obj.display())
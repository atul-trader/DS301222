class node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

class linkedlist:
    def __init__(self,head=None):
        self.head = head

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def append(self,data):
        new_node = node(data,self.head) # 3 , None  | 6, 1010
        self.head = new_node # 3,None

    # 3,1010  6,1110  5,1000  10,1001  89,0001
    def display(self):
        itr = self.head # 3,1010
        while itr:
            print(itr.data) # 3   6     5 
            itr = itr.link  # 1010 1110 1000

    def size(self):
        pass

obj = linkedlist()
print(obj.isEmpty())
obj.append(3)
obj.append(6)
obj.append(5)
obj.append(10)
obj.append(89)
obj.display()


    

    
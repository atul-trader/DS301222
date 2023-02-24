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
        obj = node(data,self.head) # 3 , None  | 6,mem_loc of 3 node | 8, mem_loc of 6 node
        self.head = obj # mem_loc of 3 node | mem_loc of 6 node | mem_loc of 8 node
        print(self.head)

    # 3,1010  6,1110  5,1000  10,1001  89,0001
    def display(self):
        itr = self.head # 3,1010
        while itr:
            print(itr.data) # 3   6     5 
            itr = itr.link  # 1010 1110 1000

    def size(self):
        count = 0 
        itr = self.head 
        while itr: 
                count += 1 
                itr = itr.link 
        return count

    # 3,6,5
    def appendleft(self,element):
        if self.isEmpty():
            self.head = node(element) # 3
            print("\ninside if : Memory Location : ",self.head," Element : ",self.head.data," Link : ",self.head.link)
            return

        itr = self.head
        print("\noutside if itr : Memory Location : ",itr," Element : ",itr.data," Link : ",itr.link)
        
        while itr.link:
            itr = itr.link
            print("inside while : ",itr)
        itr.link = node(element) # 5
        print("\noutside while : Memory Location : ",itr," Element : ",itr.data," Link : ",itr.link)



obj = linkedlist()
# print(obj.isEmpty())
# obj.append(3)
# obj.append(6)
# obj.append(5)
# obj.append(10)
# obj.append(89)
# obj.display()

# print("Size : ",obj.size())

print(obj.isEmpty())
obj.appendleft(3)
obj.appendleft(6)
obj.appendleft(5)
obj.display()

print("Size : ",obj.size())

    

    
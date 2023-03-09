class node:
    def __init__(self,element,location=None):
        self.element = element
        self.location = location


class linkedlist:
    def __init__(self,new_node=None):
        self.new_node = new_node

    def append(self,element):
        node_obj = node(element,self.new_node) # 20,None || 21,0x000002562E7A2F20 || 22,0x000001777E742EC0
        print(node_obj)
        self.new_node = node_obj #  0x000002562E7A2F20 || 0x000001777E742EC0 || 0x00000243D1C42E60

    def display(self):
        while self.new_node:
            print(self.new_node.element) # 22 || 21 || 20
            self.new_node = self.new_node.location # 0x000001777E742EC0 || 0x000002562E7A2F20 || None


linkedlist_obj = linkedlist()
linkedlist_obj.append(20)
linkedlist_obj.append(21)
linkedlist_obj.append(22)

linkedlist_obj.display()
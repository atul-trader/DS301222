# private members are not accessible to the child class

class Dad:
    def __init__(self,username,__password):
        self.username = username
        self.__password = __password

    def car(self):
        print("Car")

    def __FD(self):
        print("FD")

class Son(Dad):
    pass

son = Son("ram_14","123456")
son.car()
# son.__FD()
print(son.username)
# print(son.__password)
class A:
    def display(self):
       print("A")

class B:
    def display(self):
        print("B")

class C(A,B):
    def display(self):
        A.display(self)
        B.display(self)
        print("C")

obj = C()
obj.display()
class A:
    def a(self):
        print("a")
    
class B(A):
    def b(self):
        print("b")

class C(A):
    def c(self):
        print("c")

class D(B):
    def d(self):
        print("d")

class E(B):
    def e(self):
        print("e")

class F(C):
    def f(self):
        print("f")

class G(E,F):
    def g(self):
        print("g")

obj_g = G()
obj_g.a()
obj_g.b()
obj_g.c()
obj_g.e()
obj_g.f()
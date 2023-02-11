# Polymorphism
# poly - many
# morphism - forms

# single entity and many forms

# types of polymorphism
# 1. Compile Time Polymorphism -> this is not supported in Python
# 2. Runtime Polymorphism

# # 1. Compile Time Polymorphism (ex. overloading)
# class Shape:
#     def area(self,side:int):
#         print("Square")
#         return side ** 2

#     def area(self,length:int,breadth:int):
#         print("Rectangle")
#         return length * breadth

#     def area(self,radius:float):
#         print("Circle")
#         return 3.14*radius**2

# shape = Shape()
# print(shape.area(6,6))



# 2. Runtime Polymorphism (ex. overriding)
# Overriding can only happen in inheritance

# Rules of override
# 1. create same name method
# 2. it should have same no .of parameters

class Dad:
    def bike(self):
        return f"Color : White || Brand : TVS"

class Child(Dad):
    def mobile(self):
        return f"Color : Black || Brand : One+"

    def bike(self):
        return f"Color : Black || Brand : TVS"

obj = Child()
print(obj.mobile())
print(obj.bike())





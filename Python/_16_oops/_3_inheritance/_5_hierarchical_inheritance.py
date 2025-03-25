# Hierarchical Inheritance - Single Parent Class and Multiple Child Classes
class dad:
    def flat(self):
        print("Flat")
    
    def car(self):
        print("Car")


class son1(dad):
    def mobile(self):
        print("Mobile")


class son2(dad):
    def bike(self):
        print("Bike")


class daughter(dad):
    def jewellery(self):
        print("Jewellery")

print("Son1 Properties : \n")
son1_obj = son1()
son1_obj.mobile()
son1_obj.flat()
son1_obj.car()

print("\nSon2 Properties : \n")
son2_obj = son2()
son2_obj.bike()
son2_obj.car()
son2_obj.flat()

print("\nDaughter Properties : \n")
daughter_obj = daughter()
daughter_obj.jewellery()
daughter_obj.car()
daughter_obj.flat()
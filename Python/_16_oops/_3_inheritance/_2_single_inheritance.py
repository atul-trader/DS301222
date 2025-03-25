# Single Inheritance -> it has single parent class and single child class

class Dad:                       # parent class
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

class Son(Dad):                 # child class
    def bike(self):
        print("Bike")

    def mobile(self):
        print("Mobile")

if __name__ == "__main__":
    son = Son()
    son.bike()
    son.mobile()
    son.car()
    son.flat()


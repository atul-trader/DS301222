# Encapsulation
# means binding attributes (variable) and behaviour (methods) into single unit (getter and setter)
# accessing private members via public environment

class car:

    def __init__(self,engine,brand,mileage):
        self.engine = engine
        self.brand = brand
        self.mileage = mileage

    def display(self):
        return f"Engine : {self.engine} \nBrand : {self.brand} \nMileage : {self.mileage}"

    # setter and getter
    def get_mileage(self):
        return self.mileage

    def set_mileage(self,mileage):
        self.mileage = mileage

    def get_engine(self):
        return self.engine

    def set_engine(self,engine):
        self.engine = engine

    def get_brand(self):
        return self.engine

    def set_brand(self,brand):
        self.brand = brand


obj = car("Diesel Engine","BMW","35kmph")
print(obj.display())

print(obj.get_mileage())

obj.set_mileage("40kmph")

print(obj.display())

print(obj.get_engine())
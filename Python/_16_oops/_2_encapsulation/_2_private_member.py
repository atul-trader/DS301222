# Private members - members (method/variable) are not accessible outside the class

class car:

    def __init__(self,__engine,brand,mileage):
        self.__engine = __engine
        self.brand = brand
        self.mileage = mileage

    def display(self):
        return f"Engine : {self.__engine} \nBrand : {self.brand} \nMileage : {self.mileage}"

    # setter and getter
    def get_mileage(self):
        return self.mileage

    def set_mileage(self,mileage):
        self.mileage = mileage

    def get_engine(self):
        return self.__engine

    def set_engine(self,engine):
        self.__engine = engine

    def get_brand(self):
        return self.engine

    def set_brand(self,brand):
        self.brand = brand


obj = car("Diesel Engine","BMW","35kmph")
print(obj.display())

print(obj.get_engine())
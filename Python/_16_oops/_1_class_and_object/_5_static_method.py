# static method - is a method, which is use to create utilities function
# it has nothing to do with class or instance variable
# it will not allow you to access instance or class variable
class calculation:

    @staticmethod
    def method(no1,no2):
        return no1 + no2

obj = calculation()
print(obj.method(10,20))
        
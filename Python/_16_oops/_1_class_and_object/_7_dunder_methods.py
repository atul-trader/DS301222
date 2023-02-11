# Dunder Method | Special Method | Magic Method

# __init__
# __str__
# __name__
# __mro__

# print(dir(list))

class special_method:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return "Hey"

    def __add__(self,another_obj): 
        return self.salary + another_obj.salary

    def __mul__(self,another_obj): 
        return self.salary * another_obj.salary

    def __len__(self):
        return len(self.name)

obj1 = special_method("Bharati",10000)
obj2 = special_method("Vivek",50000)

print(obj1 + obj2)

print(obj1 * obj2)

print(len(obj2))
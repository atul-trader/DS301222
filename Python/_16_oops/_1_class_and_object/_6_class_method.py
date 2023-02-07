# class methods 
# - allows you to deal with class variable
# - takes 'cls' as a parameter
# - it will not allow you to access instance variable
# - @classmethod is a decorator, which tells pvm that method with which it is applied is class method

class school:

    school_name = "Edyoda"            # class / static variable

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @classmethod
    def set_school_name(cls,school_name):
        cls.school_name = school_name

    def display(self):
        print(f"Hi {self.name}! Your roll no is {self.rno} and you are at {school.school_name}") 
        
        
obj = school("Bharati",100)
obj.display()
print(school.get_school_name())

school.set_school_name("Coder")
print(school.get_school_name())

obj1 = school("Deepak",110)
obj1.display()
# local variable 
# global variable

# instance variable 
# - is a variable which has "self." as prefix. Example : self.name
# - scope - throughout the class  
# - it can be defined inside methods/constructor
# - every instance variable gets a seperate memory


# class/static variable
# - this variable is defined inside the class but outside the methods/constructor
# - scope : throughtout the class
# - it is accessed using class name
# - every static variables shares the same memory
# - static variable are used for memory management

class school:

    school_name = "Edyoda"            # class / static variable

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    def display(self):
        print(f"Hi {self.name}! Your roll no is {self.rno} and you are at {school.school_name}") #fstring


school_obj1 = school("Vivek",90)
school_obj1.display()

school_obj2 = school("Raj",100)
school_obj2.display()

school_obj3 = school("Ram",900)
school_obj3.display()
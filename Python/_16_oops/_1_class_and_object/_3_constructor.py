# Constructor
# it a special method
# it is created with the name __init__()
# it is use to create object
# and it is use to initialize instance variable
# it get's automatically called when object is created

# It is not recommended to write logics in constructor bcz constructor gets called everytime an object is created

# Types of Contructor
# 1. Zero Constructor ---> is a constructor with no parameters
# 2. Parameterized Constructor ---> is a constructor with parameters
# 3. Default Constructor ---> when we don't create a constructor in a class, then a default constructor is provided


class student:

    def __init__(self,name,rno):     # constructor
        self.name = name
        self.rno = rno

    def display(self):               # instance methods
        print("Name : ",self.name)
        print("Rno : ",self.rno)

student_obj = student("Deepak",20)
student_obj.display()

student_obj1 = student("Bharati",50)
student_obj1.display()

# student_obj.__init__()



    
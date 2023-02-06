# Constructor
# it a special method
# it is created with the name __init__()
# it is use to create instance
# and it is use to initialize instance variable
# it get's automatically called when object is created


class student:

    def __init__(self,name,rno):     # contructor
        self.name = name
        self.rno = rno

    def display(self):
        print("Name : ",self.name)
        print("Rno : ",self.rno)


student_obj = student("Deepak")
student_obj.display()

student_obj1 = student("Bharati",50)
student_obj1.display()

# student_obj.__init__()

    

    
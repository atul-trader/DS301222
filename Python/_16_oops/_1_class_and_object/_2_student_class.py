class student:

    def student_info(self):
        self.name = input("Enter the Name: ")
        self.rollNumber = int(input("Enter The Roll Number: "))
        

    def student_details(self):
        self.gender = input("Enter The Gender: ")
        self.dob =    input("Enter DoB: ")
        self.address = input("Enter The Address: ")
        

    def display(self):
         print("Name: ",self.name) 
         print("Roll Number: ",self.rollNumber) 
         print("Gender: ",self.gender) 
         print("DoB: ",self.dob) 
         print("Address: ", self.address)

stu = student()

stu.student_info()
stu.student_details()
stu.display()
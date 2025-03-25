# self 
# - is a keyword which represents object of the current class

# instance is an another word for object

# instance variable 
# - is a variable which has "self." as prefix
# - scope - throughout the class  

class building:                   # created a class 

    def doors(self,no_of_doors):
        self.doors = no_of_doors
        print(self.doors," Doors! --> from doors method")

    def windows(self):
        print("24 Windows!")
        print(self.doors," Doors! --> from windows method")

building_obj = building()         # created an object
no = int(input("Enter the no. of doors : "))
building_obj.doors(no)
building_obj.windows()







# self - represents current class object
# super - represents immediate parent class object

class Dad:                       
    def __init__(self,name,age):
       self.name = name
       self.age = age

    def display(self):
        return f"Name : {self.name}, Age : {self.age}"

class Son(Dad):
    def __init__(self,name,age,occupation):                 
        super().__init__(name,age)
        self.occupation = occupation

    def son_occ(self):
        return f"Son's Occupation : {self.occupation}"
  
if __name__ == "__main__":
    son = Son("Ram",45,"Student")
    print(son.son_occ())
    print(son.display())
   

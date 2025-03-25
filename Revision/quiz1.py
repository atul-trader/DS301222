class sales:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
sam=sales(100,"Deepak")
sam.__dict__['age']=49 # dict

print(sam.age + len(sam.__dict__))

# sam = {
#     "id":100,
#     "name":"Deepak",
#     "age":49
# }

# "a" + "b" =  ab
# "Bharati" * 3 = "BharatiBharatiBharati"
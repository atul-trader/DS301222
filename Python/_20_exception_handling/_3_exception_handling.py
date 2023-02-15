# name = None
# print(len(name))

name = None
try:
    print(len(name))
except Exception as ex:
    print("Exception occurs: ",ex)
    name = input("Enter a name 'which can't be None': ")
    print(len(name))

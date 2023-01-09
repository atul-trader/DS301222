# Type Conversion

# int()
# float()
# str()
# complex()
# bool()
# list()
# tuple()
# set()
# dict()

# True - 1
# False - 0

# no = 90

# print("og no : ",no,type(no))
# print("int into int : ",int(no),type(int(no)))
# print("int into str : ",str(no),type(str(no)))
# print("int into float : ",float(no),type(float(no)))
# print("int into complex : ",complex(no),type(complex(no)))
# print("int into bool : ",bool(no),type(bool(no)))


# name = "edyoda123"

# print("og name : ",name,type(name))
# print("str into int : ",int(name),type(int(name)))
# print("str into str : ",str(name),type(str(name)))
# print("str into float : ",float(name),type(float(name)))
# print("str into complex : ",complex(name),type(complex(name)))
# print("str into bool : ",bool(name),type(bool(name)))


# no = 90.89

# print("og no : ",no,type(no))
# print("float into int : ",int(no),type(int(no)))
# print("float into str : ",str(no),type(str(no)))
# print("float into float : ",float(no),type(float(no)))
# print("float into complex : ",complex(no),type(complex(no)))
# print("float into bool : ",bool(no),type(bool(no)))


# no = False

# print("og no : ",no,type(no))
# print("bool into int : ",int(no),type(int(no)))
# print("bool into str : ",str(no),type(str(no)))
# print("bool into float : ",float(no),type(float(no)))
# print("bool into complex : ",complex(no),type(complex(no)))
# print("bool into bool : ",bool(no),type(bool(no)))


# no = 8+1j
# print("og no : ",no,type(no))
# # print("complex into int : ",int(no),type(int(no)))
# print("complex into str : ",str(no),type(str(no)))
# # print("complex into float : ",float(no),type(float(no)))
# print("complex into complex : ",complex(no),type(complex(no)))
# print("complex into bool : ",bool(no),type(bool(no)))


lst = [7,8,2,1,4,4,1]
unique_value = set(lst)
unique_lst = list(unique_value)
print(unique_lst)
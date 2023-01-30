file = open("demo.txt","w")
# data = file.read()    # reads the whole file
# print(data)

# data = file.read(5)     # reads only 5 characters
# print(data)

# data = file.readline()   # reads the first line
# print(data)

# data = file.readlines()    # returns the list of lines
# print(data)

# for i in data:
#     print(i)

lst = ["Hello All\n","Good Night\n","Bye"]
file.writelines(lst)

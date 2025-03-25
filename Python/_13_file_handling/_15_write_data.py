size = int(input("Enter the size of elements you want to add in list : "))

lst = [] # list()
for i in range(size):
    element = input("Enter element : ")
    lst.append(element)


print(lst)

file = open("store.txt","a+")
for i in lst:
    file.write(i+"\n")

file.seek(0,0)

data = file.read()
print("Data : ",data)
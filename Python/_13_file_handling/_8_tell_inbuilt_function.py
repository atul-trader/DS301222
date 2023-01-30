# tell() -> it returns the current position of the cursor in the file
file = open("demo.txt","w")

position = file.tell()
print(position)

file.write("Python \nAbc")

position = file.tell()
print(position)


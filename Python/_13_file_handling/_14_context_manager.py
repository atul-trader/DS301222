# context manager - it automatically closes the file

file = open("demo.txt","w")
print(file.closed)



with open("demo.txt","w") as file:
    file.write("Hii All!")
    
print(file.closed)



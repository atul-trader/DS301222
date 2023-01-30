file = open("demo.txt","r+")


file.write("Good Evening!")
file.seek(0,0)
data = file.read()
print(data)
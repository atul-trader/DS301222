import os

# delete the file
# os.remove("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\demo.txt")

# checks if the file is present in the system
# is_exists = os.path.exists("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\test.txt")
# print("Is exist : ",is_exists)

# deletes the folder but only if it is empty
# os.rmdir("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Python\\delete_me")

# x mode
file = open("newfile1.txt","x")
file.write("Bharati")
file = open("demo.txt")
# file.close()

is_close = file.closed
print("Is close : ",is_close)

file_name = file.name
print("File Name : ",file_name)

file_mode = file.mode
print("File Mode : ",file_mode)
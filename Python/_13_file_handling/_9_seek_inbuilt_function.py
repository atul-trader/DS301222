# seek() - it allows to change the position of cursor in the file

# seek(offset,from_what)
# offset  -> no. of position to move forward
# fromwhat -> point of reference (bydefault 0)

# fromwhat
# 0 - text/binary file   -> beginning of the file
# 1 - binary file        -> current position of the file
# 2 - binary file        -> end of the file

file = open("demo.txt","w")
cur_pos = file.tell()
print("Current position before : ",cur_pos)
file.seek(10,0)
cur_pos = file.tell()
print("Current position after : ",cur_pos)
file.write("Bharati")

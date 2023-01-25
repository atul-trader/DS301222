# types of variable

# 1. local variable
# are the variables which are define inside the function
# it's scope is within the function itself
# even the arguments/parameters of the function are local variable

# 2. global variable
# are the variable which are define outside the function
# it's scope is throughout the python file


address = "Mumbai"                # global variable
def info():
    rno = 90                      # local variable
    name = "Bharati"
    print("Roll No : ",rno)
    print("Name : ",name)
    print("Function Address : ",address)

info()
print("Address : ",address)

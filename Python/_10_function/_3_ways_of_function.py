# function without any parameter and without any return statement
def addition():             
    no1 = int(input("Enter a no1 : "))
    no2 = int(input("Enter a no2 : "))
    add = no1 + no2 
    print("Addition : ",add)

# addition()


# function without any parameter and with return statement
def substraction():
    no1 = int(input("Enter a no1 : "))
    no2 = int(input("Enter a no2 : "))
    sub = no1 - no2 
    return sub

# data = substraction()
# print("Subtraction : ",data)



# function with parameter/argument and without any return statement
def multiplication(no1,no2):
    mul = no1 * no2
    print("Multiplication : ",mul)

# no1 = int(input("Enter a no1 : "))
# no2 = int(input("Enter a no2 : "))
# multiplication(no1,no2)



# function with parameter/argument and with return statement
def multiplication(no1,no2):
    mul = no1 * no2
    return mul

no1 = int(input("Enter a no1 : "))
no2 = int(input("Enter a no2 : "))
data = multiplication(no1,no2)
print("Multiplication : ",data)
# types of argument

# 1. required/positional argument
# 2. default argument
# 3. keyword argument
# 4. variable-length argument
#   4.1 Arbitrary positional argument
#   4.2 Arbitrary keyword argument



# # required/positional argument
# def add(no1,no2):
#     return no1 + no2

# print(add(5,10))



# # default argument
# def add(no1,no2=90,no3=40):
#     return no1 + no2

# print(add(100,100,100))



# # keyword argument
# def add(no1,no2):
#     print(no1,no2)
#     return no1 + no2

# print(add(no2=90,no1=87))




# # 4. variable-length argument
# #   4.1 Arbitrary positional argument
# #  *args
# #  it considers the argument as tuple

# def users(*args):
#     print(args)
#     print(type(args))
#     for i in args:
#         print(i)

# users(1,2,3,4,5,"Bharati","Edyoda",8.9,True)




# # 4. variable-length argument
# #   4.2 Arbitrary keyword argument
# #  **kwargs
# #  it considers the argument as dict

def users(**kwargs):
    print(kwargs)
    print(type(kwargs))
  

users(no2=90,no1=87,name="Bharati")







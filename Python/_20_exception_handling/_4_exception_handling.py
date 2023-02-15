# lst = [7,5,3,55,7]
# print(lst[5])

# lst=[7,5,3,55,7]
# try:
#     print(lst[5])
# except Exception as ex:
#     print("Exception : ",ex)
#     user_in=int(input("Enter an element to be added : "))
#     lst.append(user_in)
#     print(lst[5])


# lst=[7,5,3,55,7]
# try:
#     print(lst[5])
# except Exception as ex:
#     size=int(input("enter the seiz of list : "))
#     for i in range(size):
#         user_in=int(input("Enter an element to be added : "))
#         lst.append(user_in)
#     print(lst[5])

try:
    lst = [7,5,3,55,7]
    print(lst[5])
except:
    print(f'you exeeded the limit of index as the list is only having {len(lst)} elements')
    ln = len(lst)
    print(f"element {lst[ln-1]} is the max limit of index")
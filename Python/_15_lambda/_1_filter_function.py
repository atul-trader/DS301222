lst = [5,6,3,2,6,8,3,2,7,9]

# def even(lst):
#     lst1 = []
#     for i in lst:
#         if i % 2 == 0:
#             lst1.append(i)
#     return lst1
# data = even(lst)
# print("Result : ",data)


def even(lst):
    return lst % 2 == 0

data = list(filter(even,lst))
print("Result : ",data)
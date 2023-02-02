lst = [6,7,3,2,5,68,89,1]

# def square(lst):
#     lst1 = []
#     for i in lst:
#         lst1.append(i**2)
#     return lst1

# data = square(lst)
# print("Result : ",data)


def square(lst):
    return lst ** 2

data = list(map(square,lst))
print("Result : ",data)
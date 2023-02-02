from functools import reduce

lst = [6,7,3,2,5,68,89,1]

# def sum_list(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum

# data = sum_list(lst)
# print("Result : ",data)


def sum_list(lst,lst1):
    return lst + lst1

data = reduce(sum_list,lst)
print("Result : ",data)







lst = ["Dog","Cat","Lion","Cheetah","donkey","Monkey"]

def dfilter(lst):
    return lst[0].lower() == "D".lower()

data = list(filter(dfilter,lst))
print("Result: ",data)


animals = ["Dog","Cat","Lion","Cheetah","Donkey","Monkey"]
def Start_D(animals):
    return animals.startswith('D')
data=list(filter(Start_D,animals))
print(data)


lst=["dog","donkey","lion","cat","cheetah","monkey"]

def fil(lst):
    return lst.startswith("do")

data=list(filter(fil,lst))
print(data)

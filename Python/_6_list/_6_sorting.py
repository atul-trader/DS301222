# size = int(input("enter size of list"))

# lst = []
# for i in range(size):
#     element = int(input("enter element :"))
#     lst.append(element)
# # [6,3,5,6,9]
# res_list = [] # 6
# count = 0
# for i in lst: # 6,3,5,9
#     if i not in res_list:
#         res_list.append(i)
#         count = count + 1   #4

# print(count)
# print(res_list)




# size = int(input("size of list: "))
# my_list = []
# for i in range(size):
#     elements = int(input("Enter the num in list: "))
#     my_list.append(elements)
# print("the list elements are:",my_list)

# new_list = set(my_list)
# print("The unique elements of the input list using set():\n")
# list_res = (list(new_list))
# for item in list_res:
#     print(item)



lst = []
size = int(input("Enter number of elements : "))
for i in range(size):
    ele = int(input())
    lst.append(ele)

res_list = lst.copy()
data = []
count = 0
for i in range(len(lst)):
    print(i)
    removed = res_list.pop(i)
    print("r : ",res_list,lst)
    if removed not in res_list:
        data.append(removed)
        count = count + 1   

print("Count : ",count)
print("Unique Values : ",data)





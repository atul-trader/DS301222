size = int(input("Size of list is:"))
lst= []
for i in range(size):
    elements = int(input("Enter numbers in list: "))
    lst.append(elements)

print("The list elements are:",lst)

high = lst[0] # 6
for i in lst:
    if i>high:
        high = i
print("the highest no. in the list is", high)

[6,7,7,8,4,6,8,9]

4,9

2
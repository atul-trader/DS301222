lst = [7,2,5,7,8,99,0,20]
print("Original List : ",lst)

lst.append(100) # allows you to add an element
print("Append : ",lst)

lst.extend([5,3,6,8]) # allows you to add multiple elements 
print("Extend : ",lst)

lst.insert(4,200)      # adds the element on a specific index position
print("Insert : ",lst)

lst1 = lst.copy()
print("Copy : ",lst1)

# lst.clear()
# print("Clear : ",lst)

lst.remove(20)           # remove the element
print("Remove : ",lst)

lst.pop()                # bydefault removes the last element
print("Pop : ",lst)

lst.pop(1)               # removes the element on the bases of index passed 
print("Pop : ",lst)

counter = lst.count(5)
print(counter)

length = len(lst)
print("Length : ",length)

lst.reverse()
print("Reverse : ",lst)

lst.sort()
print("Sort : ",lst)

lst.sort(reverse=True) # 1
print("Sort : ",lst)

index_demo = lst.index(100)
print("Index : ",index_demo)

data = dir(list)
print(data)
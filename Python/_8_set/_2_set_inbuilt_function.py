set_demo = {5,3,100,4,66,89}
set_demo1 = {6,2,5,7,8,100}

print(set_demo)
print(set_demo1)

# intersection_demo = set_demo.intersection(set_demo1)
# print("Intersection : ",intersection_demo)

# difference_demo = set_demo.difference(set_demo1) # set_demo - set_demo1
# print("Difference : ",difference_demo)

# set_demo.intersection_update(set_demo1)
# print("Intersection Update : ",set_demo)

# set_demo.difference_update(set_demo1)
# print("Difference Update : ",set_demo)

# is_subset = set_demo.issubset(set_demo1) # it will check if all the elements of set_demo is present in set_demo1
# print("Is subset : ",is_subset)

# is_superset = set_demo.issuperset(set_demo1)
# print("Is superset : ",is_superset)

# set_demo.add(10)
# print(set_demo)

# set_demo.pop()   # bydefault removes the first element
# print(set_demo)

# set_demo.remove(4)
# print(set_demo)

# _set = set_demo.copy()
# print(_set)

# set_demo.clear()
# print(set_demo)

# set_demo.remove(101)
# print(set_demo)

set_demo.discard(101)
print(set_demo)
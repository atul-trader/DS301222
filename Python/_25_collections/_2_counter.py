# Counter

# it's a child class of dict class
# it will consider the elements as key
# and count of the element as value


# ["a","a","b","a","c","c"]

# {"a":3,"b":1,"c":2}

from collections import Counter

lst = ["a","a","b","a","c","c"]

counter = Counter(lst)
print(counter)

counter = Counter(a=4,b=2,c=9)
print(counter)

counter = Counter({"a":3,"b":1,"c":2})
print(counter)
# slicing operator [:]
# it is use to get the substring from a string
# syntaxx [start_range:end_range:step]
# step is bydefault = 1
# start is bydefault = 0
# end is bydefault = end of string

str1 = "Python is a high level programming language"
print(str1)

substring = str1[0:6]
print(substring)

substring = str1[17:22]
print(substring)

substring = str1[:22] # bydefault start_range = 0
print(substring)

substring = str1[3:]
print(substring)

substring = str1[:]
print(substring)

substring = str1[-2:]
print(substring)

substring = str1[0:6:4]
print(substring)

substring = str1[::-1]
print(substring)



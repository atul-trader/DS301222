import re

# data = "Python"
# res = re.findall("[yobh]",data) # checks if string contains "y" | "o" | "b" | "h"
# print(res)

# data = "Python"
# res = re.findall("[^npa]",data) # Returns a match for any character EXCEPT "n" | "p" | "a"
# print(res)


# data = "357897346"
# res = re.findall("[389]",data) # Returns a match for any character "3" | "8" | "9"
# print(res)


# data = "Python"
# res = re.findall("[a-z]{9}",data) 
# print(res)


# data = "ython"
# res = re.findall("^[a-z]{5}$",data) 
# print(res)


# data = "ython@5387"
# res = re.findall("^[a-z]{5}[@]\d{5}$",data) 
# print(res)


data = "78"
res = re.findall("[0-8][5-9]",data)
print(res)


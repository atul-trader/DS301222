import re

# data = "Python is high level programming langauge"
# res = re.findall("\APython",data) # checks if string starts with "Python"
# print(res)


# data = "Python is high level programming langauge"
# res = re.findall("Python\Z",data) # checks if string ends with "Python"
# print(res)


# data = "Python is high level programming langauge Pycharm"
# res = re.findall(r"\bPy",data) # checks for all the words starts with "Py"
# print(res)


# data = "Python is high level programming langauge charming"
# res = re.findall(r"\Bing",data) # checks for all the words ends with "ing"
# print(res)


# data = "Python is high level programming langauge 123"
# res = re.findall(r"\d",data) # returns digits
# print(res)


# data = "Python is high level programming langauge Pycharm 123"
# res = re.findall(r"\D",data) # returns non-digits
# print(res)


# data = "Python is high level programming langauge Pycharm"
# res = re.findall(r"\s",data) # checks for all spaces
# print(res)


# data = "Python is high level programming langauge Pycharm"
# res = re.findall(r"\S",data) # checks for all non-spaces characters
# print(res)


# data = "Python 123 _ @@@ !!!"
# res = re.findall(r"\w",data) # checks for all A-Z,a-z,0-9,_
# print(res)



data = "Python 123 _ @@@ !!!"
res = re.findall(r"\W",data) # checks for all A-Z,a-z,0-9,_
print(res)
import re 

# data = "Hello"
# res = re.findall("[a-z]",data) # checks for small letters
# print(res)


# data = "Hello"
# res = re.findall("[A-Z]",data) # checks for capital letters
# print(res)


# data = "Hello123"
# res = re.findall("[A-z]",data) # checks for letters
# print(res)


# data = "Hello"
# res = re.findall("[A-Za-z]",data) # checks for letters
# print(res)


# data = "Hello"
# res = re.findall("[a-e]",data) # checks for small letters in specified range
# print(res)


# data = "Hello"
# res = re.findall("[A-E]",data) # checks for capital letters in specified range
# print(res)


# data = "Hello123"
# res = re.findall("\d",data) # checks for digits
# print(res)


# data = "Hello Bharati"
# res = re.findall("H...o",data) # checks for string which starts with 'H' and ends with 'o' and inbetween any 3 characters
# print(res)


# data = "Helo"
# res = re.findall("He.*o",data) # checks for string which starts with 'He' and ends with 'o' and inbetween any 0 or more characters
# print(res)


# data = "Heo"
# res = re.findall("He.+o",data) # checks for string which starts with 'He' and ends with 'o' and inbetween any 1 or more characters
# print(res)


# data = "Hello"
# res = re.findall("He.?o",data) # checks for string which starts with 'He' and ends with 'o' and inbetween any 0 or 1 characters
# print(res)


# data = "Hello"
# res = re.findall("He.{2}o",data) # checks for string which starts with 'He' and ends with 'o' and inbetween any 2 characters
# print(res)


# data = "Python is a language"
# res = re.findall("lang",data) # checks for string contains "is"
# print(res)


# data = "Python is a language"
# res = re.findall("is|lang|bharati",data) # checks for string "is" or "lang" or "bharati"
# print(res)


# data = "Python is a language"
# res = re.findall("^P",data) # checks for string starts with "P"
# print(res)


# data = "Python is a language"
# res = re.findall("language$",data) # checks for string ends with "language"
# print(res)
import re

email = input("Enter email ID : ")

res = re.findall("^[a-zA-Z0-9._]+[@]{1}[a-z]+[.]{1}[a-z]+$",email)

if res:
    print("Correct Email Format!")
else:
    print("Incorrect Email Format!")




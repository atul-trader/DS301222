import re

code = input("Enter pin code: ")

res = re.findall("^[1-9]{1}[0-9]{5}$",code)
if res:
    print("Entered pin code is valid.")
else:
    print("Please enter a valid pin code.")



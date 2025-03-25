import re
pen = input("enter your pen: ")
res= re.findall ("^[A-Z]{5}[0-9]{4}[A-Z]{1}$",pen)

if res:
    print("verified")
else:
    print("not verified")


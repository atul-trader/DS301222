import re
mobile=input("enter your mobile number ")
res= re.findall("^[1-9]{1}[0-9]{9}$",mobile)
if res:
    print("the mobile no.  is valid")
else:
    print("the mobile no. is not valid")
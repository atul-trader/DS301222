import re
password_check=input("enter ur password : ")
res=re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$",password_check)
if res: 
    print("your password is correct")
else:
    print("pls enter correct password")
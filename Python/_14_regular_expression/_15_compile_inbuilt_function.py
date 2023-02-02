import re
password_check=input("enter ur password : ")
pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$")
res=re.findall(pattern,password_check)
if res: 
    print("your password is correct")
else:
    print("pls enter correct password")






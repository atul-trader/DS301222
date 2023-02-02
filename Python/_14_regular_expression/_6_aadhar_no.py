import re 

aadhar_num = input("enter the aadhar number :")
res = re.findall("^[1-9]{1}[0-9]{3}[-][0-9]{4}[-][0-9]{4}$",aadhar_num)
if res:
    print ("aadhar number is valid")
else:
    print ("aadhar number is not valid")

pan no

5 capital characters , 4 numbers , 1 capital character
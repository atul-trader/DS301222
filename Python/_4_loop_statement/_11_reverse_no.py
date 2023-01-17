i = int(input("enter number")) # 634 == 436
rev = 0
while (i>0):
    mod = i%10               # 4
    rev=mod
    i=i//10

print("reverse=",rev)

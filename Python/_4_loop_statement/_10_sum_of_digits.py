num=int(input("Enter a number to find sum of number:"))   # 623
total = 0
while(num>0):
    mod=num%10       # 3   2   6
    total=total+mod  # 3   5   11
    num=num//10      # 62  6   0
print("The total sum of digits is:",total)



i = int(input("enter number")) # 421 == 124
rev = 0
while (i>0):
    mod = i % 10               # 1      # 2     # 4 
    rev = rev * 10 + mod       # 1      # 12    # 124
    i = i//10                  # 42     # 4     # 0
print("reverse=",rev)


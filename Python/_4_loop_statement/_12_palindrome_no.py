i = int(input("enter number : ")) 
og = i
rev = 0
while (i>0):
    mod = i % 10              
    rev = rev * 10 + mod       
    i = i//10                 
print("reverse=",rev)


if og == rev:
    print("It's a palindrome no.")
else:
    print("It's not a palindrome no.")
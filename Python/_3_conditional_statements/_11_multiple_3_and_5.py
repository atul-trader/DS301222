num=int(input("please enter number to check wheather divisible by 3 and 5  = "))
 
if num%3==0 and num%5==0:
    print("number is divisible by both",num)
elif num%3==0:
    print("only divisible by 3",num)   
elif num %5==0:
    print("only divisible by 5",num)    
else:
    print("not divisible by 3 and 5") 



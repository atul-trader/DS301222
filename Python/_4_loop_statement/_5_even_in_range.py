start_range=int(input("enter the start range :"))
end_range=int(input("enter the end range :"))

print("all tha even values between ",start_range,"and",end_range,"are :")

for i in range(start_range,end_range+1):
    if i%2==0:
        print(i)







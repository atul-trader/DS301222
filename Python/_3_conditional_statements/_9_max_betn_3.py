no1 = int(input("Enter your first no."))
no2 = int(input("Enter your second no."))
no3 = int(input("Enter your third no."))

if no1 > no2 and no1 > no3:
    print(no1,'no1 is the largest number')
elif no2 > no1 and no2 > no3:
    print(no2,'no2 is the largest number')
else:
    print(no3,'no3 is the largest number')

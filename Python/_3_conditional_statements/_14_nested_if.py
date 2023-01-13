# Girl's College

gender = input("Enter your gender (enter F for Female and M for Male): ")
cut_off = 60
if gender == "F":
    qualification = int(input("Enter your qualification (enter 10 for 10th) : "))
    if qualification == 10:
        percentage = float(input("Enter your 10th percentage : "))
        if percentage >= 60:
            print("Congratulations! You are eligible!")
        else:
            print("Sorry you have not passed the college cut-off")
    else:
        print("We only provide jr. college admission here!")
else:
    print("This is girl's college, hence only girls are allowed!")




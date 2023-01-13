rlno=int(input("enter roll number : "))
name=input("enter name : ")
maths_marks = int(input("enter maths marks : "))
english_marks = int(input("enter english marks : "))
science_marks = int(input("enter science marks : "))
fix_total= 300 
total= maths_marks + english_marks + science_marks
percentage = total / fix_total * 100

if percentage >= 90:
    grade = "A"
elif percentage >=80 and percentage<90:
	grade = "B"
elif percentage >=70 and percentage<80:
	grade = "C"
elif percentage >=60 and percentage <70:
	grade = "D"
elif percentage>=50 and percentage<60:
    grade = "E"
elif percentage>=40 and percentage<50:
	grade = "E+"
else: 
    grade = "F"

print("****************Report Card******************")
print("Name : ",name, "\nRoll No : ",rlno,"\nMaths Marks : ",maths_marks,"\nEnglish Marks : ",english_marks,"\nScience Marks : ",science_marks,"\nTotal Marks : ",total,"\nPercentage : ",percentage,"\nGrade : ",grade)




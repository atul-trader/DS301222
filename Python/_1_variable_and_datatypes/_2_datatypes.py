# Datatype
# the type of data the variable is storing

# int    - digit
# float  - decimal
# str    - character, word, statement, para
# bool   - True / False
# complex - real + imaginary
# NoneType - void

# Type Function - returns the datatype of variable passed inside the function

# immutable
# num = 10
# num_type = type(num)
# print("Num Type :",num_type)

# immutable
# name = "Bharati"
# name_type = type(name)
# print("Name Type : ",name_type)

# immutable
# salary = 10000.50
# salary_type = type(salary)
# print("Salary Type : ",salary_type)

# immutable
# qualified = True
# qualified_type = type(qualified)
# print("Qualified Type : ",qualified_type)

# immutable
# eq = 1 + 1j
# eq_type = type(eq)
# print("Eq Type : ",eq_type)


# future_idea = None
# future_idea_type = type(future_idea)
# print("Future Idea Type : ", future_idea_type)


# Collection
# list
# tuple
# set
# dict

# list
# []
# it is indexed based (indexing starts with 0)
# it supports heterogenous data (values with different datatypes)
# it is ordered
# it is mutable (modifiable)
# it allows to store duplicate values
# student_names = ["ram","raj","sita","gita","rohit",78,90.6,True,78]
# print(student_names)
# print(student_names[3])
# student_names[4] = "rohan"
# print(student_names)


# tuple
# ()
# it is indexed based (indexing starts with 0)
# it supports heterogenous data (values with different datatypes)
# it is ordered
# it is immutable
# duplicates are allowed
# rnos = (5,4,7,2,3,6,7.77,"edyoda",5)
# print(rnos)
# print(rnos[0])


# set
# {}
# it is unordered
# it is non-indexed
# it supports heterogenous data (values with different datatypes)
# it is mutable
# duplicates are not allowed
rnos = {4,5,21,6,87,100,"Bharati",100}
rnos.add(450)
print(rnos)


# dict
# {key:value} => item
# keys should be unique
# values can be duplicate
# non-indexed
# it stores heterogenous
# it is unordered
# it is mutable
# students = {"a":"Ram",90:"Raj","b":5.6}
# print(students)

# students[90] = "Rohan"
# print(students)


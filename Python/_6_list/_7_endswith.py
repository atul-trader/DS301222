range1=int(input("enter the range of no of elements : "))
lst=[]
for i in range(range1):
    element=input("enter the elements of the list : ")
    lst.append(element)
    
print("the list is : ",lst)

lst1=[]
for i in lst:
    if i.endswith("at"):
        lst1.append(i)
print(lst1)
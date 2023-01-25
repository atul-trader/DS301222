choice=int(input("enter your choice to calculate its area \n 1. Square \n 2. Rectangle \n 3. Circle \n 4. Triangle  : "))

def area_square():
    size=int(input("enter size : "))
    area_sq=size**2
    return area_sq

def area_rectangle():
    length=int(input("enter length : "))
    breadth=int(input("enter breadth : "))
    area_rect=length*breadth
    print("area of rectangle is : ",area_rect)
   
def area_circle():
    radius=int(input("enter radius : "))
    area_cir=(22*radius**2)/7
    return area_cir
    
def area_triangle():
    length=int(input("enter length : "))
    height=int(input("enter height : "))
    area_tri=(length*height)/2
    print("area of square is : ",area_tri)
    
if choice ==1:
    area1=area_square()
    print("area of square is : ",area1)
    
if choice ==2:
    area_rectangle()
    
if choice ==3:
    area2=area_circle()
    print("area of cicle is ",area2)
    
if choice==4:
    area_triangle()
length=int(input("enter length :"))
breadth=int(input("enter breadth :"))

if length==breadth:
    print("The dimensions are of a square")
elif length == 0 and breadth == 0:
    print("Shape unidentifiable")
else:
    print("The dimensions are of a rectangle")
